import os
import sys
import json
import httpx
from typing import AsyncGenerator
from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models import BaseLlm, LlmRequest, LlmResponse
from google.genai import types

# .env 파일 로드: 1) 현재 작업 디렉토리, 2) 현재 파일의 부모 폴더 (hands-on/session-1/work)
load_dotenv()
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(parent_dir, ".env"))

class OllamaChatLlm(BaseLlm):
    """로컬 Ollama 서버의 Gemma 4 모델과 비동기적으로 통신하는 커스텀 LLM 어댑터"""
    api_base: str

    @classmethod
    def supported_models(cls) -> list[str]:
        # 모든 모델 패턴을 수용
        return [".*"]

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ) -> AsyncGenerator[LlmResponse, None]:
        url = f"{self.api_base}/api/chat"
        headers = {"Content-Type": "application/json"}

        # 1. System Instruction 파싱 및 추출
        system_instruction = ""
        if llm_request.config and llm_request.config.system_instruction:
            si = llm_request.config.system_instruction
            if isinstance(si, str):
                system_instruction = si
            elif hasattr(si, "parts") and si.parts:
                parts_text = [p.text for p in si.parts if hasattr(p, "text") and p.text]
                system_instruction = "".join(parts_text)

        # 2. 메시지 리스트 빌드
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})

        for content in llm_request.contents:
            role = "assistant" if content.role == "model" else content.role
            parts_text = [p.text for p in content.parts if hasattr(p, "text") and p.text]
            text = "".join(parts_text)
            messages.append({"role": role, "content": text})

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": stream
        }

        # 3. 사전 모델 검사 (GET /api/tags)
        tags_url = f"{self.api_base}/api/tags"
        try:
            async with httpx.AsyncClient(timeout=10.0) as check_client:
                response = await check_client.get(tags_url)
                response.raise_for_status()
                tags_data = response.json()
        except httpx.ConnectError:
            raise RuntimeError(
                f"오류: Ollama 서버({self.api_base})에 연결할 수 없습니다. 서버가 켜져 있는지 확인하세요."
            )
        except Exception as e:
            raise RuntimeError(
                f"오류: Ollama 서버 상태를 확인하는 과정에서 예외가 발생했습니다. ({e})"
            )

        available_models = [m.get("name") for m in tags_data.get("models", [])]
        if self.model not in available_models:
            error_msg = (
                f"오류: 지정된 모델 '{self.model}'이 Ollama 서버에 설치되어 있지 않습니다.\n"
                f"해결 방법:\n"
                f"  1. 다음 터미널 명령을 실행하여 필요한 모델을 다운로드하세요:\n"
                f"     ollama pull {self.model}\n"
                f"  2. 또는 '.env' 파일의 'ADK_OLLAMA_MODEL' 설정을 수정하거나 다운로드된 올바른 모델명을 사용하세요.\n"
                f"\n현재 사용 가능한 모델 목록:\n"
            )
            if available_models:
                error_msg += "\n".join(f"  - {m}" for m in available_models)
            else:
                error_msg += "  (다운로드된 모델이 없습니다)"
            raise ValueError(error_msg)

        # 4. 스트리밍 / 비스트리밍 호출 및 응답 처리
        timeout = 180.0
        if stream:
            full_response_text = ""
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    async with client.stream("POST", url, json=payload, headers=headers) as response:
                        response.raise_for_status()
                        async for line in response.aiter_lines():
                            if not line.strip():
                                continue
                            data = json.loads(line)
                            content_chunk = data.get("message", {}).get("content") or ""
                            full_response_text += content_chunk

                            # 스트리밍 중간 청크 yield (partial=True)
                            yield LlmResponse(
                                content=types.Content(
                                    role="model",
                                    parts=[types.Part(text=content_chunk)]
                                ),
                                partial=True,
                                turn_complete=False
                            )

                # 스트리밍 정상 종료 시 누적된 전체 텍스트 yield (partial=False, turn_complete=True)
                yield LlmResponse(
                    content=types.Content(
                        role="model",
                        parts=[types.Part(text=full_response_text)]
                    ),
                    partial=False,
                    turn_complete=True
                )
            except Exception as e:
                raise RuntimeError(f"오류: API 호출 중 예상치 못한 문제가 발생했습니다. ({e})")
        else:
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.post(url, json=payload, headers=headers)
                    response.raise_for_status()
                    data = response.json()
                    content_text = data.get("message", {}).get("content") or ""

                    # 단일 최종 응답 반환
                    yield LlmResponse(
                        content=types.Content(
                            role="model",
                            parts=[types.Part(text=content_text)]
                        ),
                        partial=False,
                        turn_complete=True
                    )
            except Exception as e:
                raise RuntimeError(f"오류: API 호출 중 예상치 못한 문제가 발생했습니다. ({e})")

# OLLAMA_API_BASE가 있으면 최우선, 없으면 OLLAMA_HOST, 그것도 없으면 기본값
api_base = os.getenv("OLLAMA_API_BASE") or os.getenv("OLLAMA_HOST") or "http://localhost:11434"
model_tag = os.getenv("ADK_OLLAMA_MODEL") or os.getenv("OLLAMA_MODEL") or "gemma4:e4b"

# ADK root_agent 선언
root_agent = LlmAgent(
    name="adk_ollama_gemma4_agent",
    model=OllamaChatLlm(model=model_tag, api_base=api_base),
    instruction=(
        "당신은 Gemma 4 로컬 모델을 사용하는 친절하고 지능적인 AI 에이전트입니다. "
        "다음 규칙에 따라 답변해 주세요:\n"
        "1. 모든 대답은 한국어로 부드럽고 명확하게 작성하세요.\n"
        "2. 구조화가 필요한 설명은 번호가 매겨진 리스트(Numbered Steps)를 적극적으로 사용해 주세요.\n"
        "3. 로컬에서 AI 모델(Ollama)을 다루고 실습하는 사용자 친화적이고 구체적인 설명과 팁을 필요시 함께 덧붙여 주세요."
    )
)
