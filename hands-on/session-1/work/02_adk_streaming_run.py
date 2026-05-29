import sys
import asyncio
from google.adk.runners import InMemoryRunner
from google.adk.agents import RunConfig
from google.adk.agents.run_config import StreamingMode
from adk_02_ollama_agent.agent import root_agent

async def main():
    # 명령줄 인수 확인 (질문 프롬프트 전달 여부)
    if len(sys.argv) < 2:
        print("사용법: uv run python 02_adk_streaming_run.py \"[질문]\"", file=sys.stderr)
        sys.exit(1)

    prompt = sys.argv[1]

    # InMemoryRunner 초기화
    runner = InMemoryRunner(agent=root_agent)

    # RunConfig 설정 (스트리밍 방식을 SSE로 지정)
    config = RunConfig(streaming_mode=StreamingMode.SSE)

    print("=" * 60)
    print(f"에이전트명: {root_agent.name}")
    print(f"사용할 모델: {root_agent.model.model}")
    print(f"질문 프롬프트: {prompt}")
    print("=" * 60)
    print()

    displayed_text = ""

    # new_message 객체 생성
    from google.genai import types
    new_message = types.Content(
        role="user",
        parts=[types.Part(text=prompt)]
    )

    # 비동기 실행 및 이벤트 수신 (keyword-only 인수 사용)
    async for event in runner.run_async(
        user_id="default_user",
        session_id="default_session",
        new_message=new_message,
        run_config=config
    ):
        if event.partial:
            # 스트리밍 중간 청크(타이프라이터 효과용)
            if event.content and event.content.parts:
                # 툴 호출(function call)이 없는 순수 텍스트 청크인지 검사
                has_text = any(part.text for part in event.content.parts)
                has_fc = any(part.function_call for part in event.content.parts)

                if has_text and not has_fc:
                    text = "".join(p.text or "" for p in event.content.parts)
                    print(text, end="", flush=True)
                    displayed_text += text
        else:
            # 최종 집계(Aggregated) 이벤트 처리
            if event.content:
                final_text = "".join(p.text or "" for p in event.content.parts)
                # 이전에 이미 출력된 스트리밍 본문과 차이가 있다면 중복 출력하지 않고 끝자리 누락분만 보정
                if final_text.strip() and final_text != displayed_text:
                    diff_text = final_text[len(displayed_text):]
                    if diff_text:
                        print(diff_text, end="", flush=True)
                        displayed_text = final_text
    print("\n")

if __name__ == "__main__":
    asyncio.run(main())
