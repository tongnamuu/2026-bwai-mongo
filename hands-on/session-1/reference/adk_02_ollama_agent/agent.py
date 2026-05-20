"""ADK agent that calls local Gemma 4 through Ollama.

Run after Ollama is running:
    cd hands-on/session-1/reference
    uv run adk run adk_02_ollama_agent
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
import os
from pathlib import Path


DEFAULT_API_BASE = "http://localhost:11434"
DEFAULT_MODEL = "gemma4:e2b"
DEFAULT_TIMEOUT = 180.0


def load_env() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return

    # ADK runs from the package, so explicitly load reference/.env as well.
    load_dotenv(Path(__file__).resolve().parents[1] / ".env")
    load_dotenv()


def choose_api_base() -> str:
    return (
        os.getenv("OLLAMA_API_BASE")
        or os.getenv("OLLAMA_HOST")
        or DEFAULT_API_BASE
    )


def choose_model() -> str:
    # ADK-specific env wins, then the general Ollama env, then the reference default.
    return (
        os.getenv("ADK_OLLAMA_MODEL")
        or os.getenv("OLLAMA_MODEL")
        or DEFAULT_MODEL
    )


load_env()

from google.adk.agents import LlmAgent
from google.adk.models import BaseLlm
from google.adk.models import LlmRequest
from google.adk.models import LlmResponse
from google.genai import types
import httpx


def content_to_text(content: types.Content | str | None) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content

    text_parts = []
    for part in content.parts or []:
        if part.text:
            text_parts.append(part.text)
    return "\n".join(text_parts)


def system_instruction_to_text(instruction: object) -> str:
    if isinstance(instruction, list):
        return "\n\n".join(system_instruction_to_text(item) for item in instruction)
    if isinstance(instruction, types.Content):
        return content_to_text(instruction)
    return str(instruction) if instruction else ""


class OllamaChatLlm(BaseLlm):
    """Tiny ADK model adapter that calls Ollama's native /api/chat endpoint."""

    api_base: str = DEFAULT_API_BASE
    timeout: float = DEFAULT_TIMEOUT

    def build_messages(self, llm_request: LlmRequest) -> list[dict[str, str]]:
        system_text = system_instruction_to_text(
            llm_request.config.system_instruction
        )
        messages = []
        if system_text:
            messages.append({"role": "system", "content": system_text})

        for content in llm_request.contents:
            text = content_to_text(content)
            if not text:
                continue
            role = "assistant" if content.role == "model" else "user"
            messages.append({"role": role, "content": text})

        return messages

    async def generate_content_async(
        self, llm_request: LlmRequest, stream: bool = False
    ) -> AsyncGenerator[LlmResponse, None]:
        if llm_request.tools_dict:
            yield LlmResponse(
                error_code="UNSUPPORTED_TOOLS",
                error_message="This simple Ollama adapter does not support ADK tools.",
            )
            return

        self._maybe_append_user_content(llm_request)
        model = llm_request.model or self.model
        payload = {
            "model": model,
            "messages": self.build_messages(llm_request),
            "stream": False,
            "options": {
                "temperature": llm_request.config.temperature or 0.3,
            },
        }

        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(
                    f"{self.api_base.rstrip('/')}/api/chat",
                    json=payload,
                    headers={"Accept": "application/json"},
                )
                response.raise_for_status()
                data = response.json()
        except Exception as exc:
            yield LlmResponse(
                error_code="OLLAMA_API_ERROR",
                error_message=f"Ollama API 호출에 실패했습니다: {exc}",
            )
            return

        answer = data.get("message", {}).get("content", "")
        yield LlmResponse(
            model_version=model,
            content=types.Content(
                role="model",
                parts=[types.Part(text=answer)],
            ),
            partial=False,
        )


# ADK discovers this variable name when running `adk run <agent_package>`.
root_agent = LlmAgent(
    model=OllamaChatLlm(model=choose_model(), api_base=choose_api_base()),
    name="adk_ollama_gemma4_agent",
    instruction=(
        "You are a local Gemma 4 workshop assistant. "
        "Answer in Korean, prefer numbered steps, and keep the explanation practical."
    ),
)
