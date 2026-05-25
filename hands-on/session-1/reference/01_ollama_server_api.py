"""Local Gemma 4 hands-on through the Ollama server API.

Run after Ollama is running:
    cd hands-on/session-1/reference
    uv run python 01_ollama_server_api.py
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


DEFAULT_HOST = "http://localhost:11434"
DEFAULT_MODEL = "gemma4:e4b"
DEFAULT_PROMPT = (
    "MongoDB 초보자에게 벡터 검색과 생성형 AI를 함께 쓰는 예시를 "
    "3단계로 설명해 주세요."
)
DEFAULT_SYSTEM = (
    "You are a concise workshop assistant. "
    "Answer in Korean and prefer numbered steps."
)


def load_env() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return

    # Load values from reference/.env first, then from the current directory.
    load_dotenv(Path(__file__).with_name(".env"))
    load_dotenv()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Call local Gemma 4 through the Ollama HTTP API."
    )
    parser.add_argument(
        "--host",
        default=os.getenv("OLLAMA_HOST", DEFAULT_HOST),
        help=f"Ollama server URL. Default: {DEFAULT_HOST}",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("OLLAMA_MODEL", DEFAULT_MODEL),
        help=f"Local Ollama model tag. Default: {DEFAULT_MODEL}",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="Prompt to send to the local model.",
    )
    parser.add_argument(
        "--system",
        default=DEFAULT_SYSTEM,
        help="System message for the local model.",
    )
    parser.add_argument(
        "--endpoint",
        choices=("ollama", "openai"),
        default="ollama",
        help="Use Ollama native /api/chat or OpenAI-compatible /v1/chat/completions.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=180,
        help="Maximum seconds to wait for the model response.",
    )
    parser.add_argument(
        "--no-stream",
        action="store_true",
        help="Print the response after completion instead of streaming tokens.",
    )
    return parser.parse_args()


def request_json(
    method: str,
    url: str,
    *,
    payload: dict[str, Any] | None = None,
    timeout: int = 30,
) -> dict[str, Any]:
    # Import httpx here so argparse --help can run before dependencies exist.
    import httpx

    with httpx.Client(timeout=timeout) as client:
        response = client.request(
            method,
            url,
            json=payload,
            headers={"Accept": "application/json"},
        )
        response.raise_for_status()
        return response.json()


def ensure_server_and_model(host: str, model: str) -> None:
    try:
        # /api/tags is a lightweight way to check both server and local models.
        data = request_json("GET", f"{host.rstrip('/')}/api/tags")
    except Exception as exc:
        print(
            f"Ollama 서버에 연결할 수 없습니다: {host}\n"
            "Ollama 앱을 실행하거나 별도 터미널에서 'ollama serve'를 실행해 주세요.\n"
            f"원인: {exc}",
            file=sys.stderr,
        )
        raise SystemExit(2) from exc

    model_names = {item.get("name") for item in data.get("models", [])}
    if model not in model_names:
        available = sorted(name for name in model_names if name)
        latest_hint = ""
        if model == DEFAULT_MODEL and "gemma4:latest" in model_names:
            latest_hint = (
                "\n참고: 현재 'gemma4:latest'만 보이면 같은 모델 계열이어도 "
                "Ollama API에서는 태그명이 달라 별도 모델로 취급합니다.\n"
                "권장: ollama pull gemma4:e4b\n"
                "바로 진행: .env에서 OLLAMA_MODEL=gemma4:latest 로 변경"
            )
        print(
            f"Ollama 서버에는 연결됐지만 {model!r} 모델이 없습니다.\n"
            f"현재 사용 가능한 모델: {available}\n"
            f"인터넷이 되는 곳에서 먼저 실행하세요: ollama pull {model}"
            f"{latest_hint}",
            file=sys.stderr,
        )
        raise SystemExit(2)


def call_ollama_chat(args: argparse.Namespace) -> str:
    payload = {
        "model": args.model,
        "messages": [
            {"role": "system", "content": args.system},
            {"role": "user", "content": args.prompt},
        ],
        "stream": not args.no_stream,
        "options": {
            "temperature": 0.3,
        },
    }
    if not args.no_stream:
        return stream_ollama_chat(args, payload)

    data = request_json(
        "POST",
        f"{args.host.rstrip('/')}/api/chat",
        payload=payload,
        timeout=args.timeout,
    )
    return data["message"]["content"]


def stream_ollama_chat(args: argparse.Namespace, payload: dict[str, Any]) -> str:
    import httpx

    chunks = []
    with httpx.Client(timeout=args.timeout) as client:
        with client.stream(
            "POST",
            f"{args.host.rstrip('/')}/api/chat",
            json=payload,
            headers={"Accept": "application/json"},
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line:
                    continue
                data = json.loads(line)
                piece = data.get("message", {}).get("content", "")
                if piece:
                    print(piece, end="", flush=True)
                    chunks.append(piece)
                if data.get("done"):
                    break
    print()
    return "".join(chunks)


def call_openai_compatible(args: argparse.Namespace) -> str:
    # Ollama also exposes an OpenAI-compatible endpoint for client portability.
    payload = {
        "model": args.model,
        "messages": [
            {"role": "system", "content": args.system},
            {"role": "user", "content": args.prompt},
        ],
        "stream": not args.no_stream,
        "temperature": 0.3,
    }
    if not args.no_stream:
        return stream_openai_compatible(args, payload)

    data = request_json(
        "POST",
        f"{args.host.rstrip('/')}/v1/chat/completions",
        payload=payload,
        timeout=args.timeout,
    )
    return data["choices"][0]["message"]["content"]


def stream_openai_compatible(args: argparse.Namespace, payload: dict[str, Any]) -> str:
    import httpx

    chunks = []
    with httpx.Client(timeout=args.timeout) as client:
        with client.stream(
            "POST",
            f"{args.host.rstrip('/')}/v1/chat/completions",
            json=payload,
            headers={"Accept": "application/json"},
        ) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if not line or not line.startswith("data: "):
                    continue
                data_text = line.removeprefix("data: ").strip()
                if data_text == "[DONE]":
                    break
                data = json.loads(data_text)
                piece = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
                if piece:
                    print(piece, end="", flush=True)
                    chunks.append(piece)
    print()
    return "".join(chunks)


def main() -> int:
    load_env()
    args = parse_args()
    # Fail fast with a friendly message before starting a long generation call.
    ensure_server_and_model(args.host, args.model)

    endpoint = "/v1/chat/completions" if args.endpoint == "openai" else "/api/chat"

    print(f"\n[host] {args.host}")
    print(f"[endpoint] {endpoint}")
    print(f"[model] {args.model}")
    print(f"[prompt] {args.prompt}\n")

    try:
        if args.endpoint == "openai":
            answer = call_openai_compatible(args)
        else:
            answer = call_ollama_chat(args)
    except Exception as exc:
        print(f"Ollama API 호출에 실패했습니다: {exc}", file=sys.stderr)
        return 1

    if args.no_stream:
        print(answer.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
