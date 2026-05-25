"""Run the ADK Ollama agent with SSE streaming in a terminal.

Usage:
    cd hands-on/session-1/reference
    uv run python 02_adk_streaming_run.py "MongoDB 벡터 검색을 3단계로 설명해 줘."
"""

from __future__ import annotations

import argparse
import asyncio
from contextlib import aclosing

from adk_02_ollama_agent.agent import root_agent
from google.adk.agents.run_config import RunConfig
from google.adk.agents.run_config import StreamingMode
from google.adk.runners import InMemoryRunner
from google.genai import types


DEFAULT_PROMPT = "MongoDB 벡터 검색을 로컬 Gemma 4와 함께 쓰는 흐름을 3단계로 설명해 줘."
USER_ID = "local-user"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run ADK Ollama agent with streaming.")
    parser.add_argument(
        "prompt",
        nargs="?",
        default=DEFAULT_PROMPT,
        help="Prompt to send to the ADK agent.",
    )
    return parser.parse_args()


async def run_streaming(prompt: str) -> None:
    runner = InMemoryRunner(
        agent=root_agent,
        app_name="adk_ollama_streaming_demo",
    )

    try:
        session = await runner.session_service.create_session(
            app_name=runner.app_name,
            user_id=USER_ID,
        )
        message = types.Content(role="user", parts=[types.Part(text=prompt)])
        run_config = RunConfig(streaming_mode=StreamingMode.SSE)
        displayed_text = ""

        async with aclosing(
            runner.run_async(
                user_id=USER_ID,
                session_id=session.id,
                new_message=message,
                run_config=run_config,
            )
        ) as events:
            async for event in events:
                if not event.content or not event.content.parts:
                    continue

                text = "".join(part.text or "" for part in event.content.parts)
                if not text:
                    continue

                if event.partial:
                    print(text, end="", flush=True)
                    displayed_text += text
                elif text != displayed_text:
                    print(text, end="", flush=True)

        print()
    finally:
        await runner.close()


if __name__ == "__main__":
    args = parse_args()
    asyncio.run(run_streaming(args.prompt))
