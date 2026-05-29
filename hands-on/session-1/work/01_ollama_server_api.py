import argparse
import os
import sys
import json
import httpx
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

def main():
    # 환경변수 우선 적용, 없으면 기본값 사용
    default_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    default_model = os.getenv("OLLAMA_MODEL", "gemma4:e4b")

    parser = argparse.ArgumentParser(description="Ollama Server API 실습 예제 (Gemma 4)")
    parser.add_argument("--host", default=default_host, help="Ollama 서버 호스트 주소")
    parser.add_argument("--model", default=default_model, help="사용할 Ollama 모델명")
    parser.add_argument("--prompt", required=True, help="모델에 전달할 질문 프롬프트")
    parser.add_argument("--system", default="You are a helpful assistant.", help="시스템 메시지 (System Prompt)")
    parser.add_argument("--endpoint", choices=["ollama", "openai"], default="ollama", help="API 엔드포인트 종류 (ollama 또는 openai)")
    parser.add_argument("--no-stream", action="store_true", help="스트리밍 출력을 끄고 응답 완료 후 한 번에 출력")
    parser.add_argument("--timeout", type=float, default=180.0, help="API 호출 제한 시간 (초)")

    args = parser.parse_args()

    host = args.host.rstrip("/")
    model = args.model
    stream = not args.no_stream
    timeout = args.timeout

    print("=" * 50)
    print(f"호스트: {host}")
    print(f"엔드포인트: {args.endpoint}")
    print(f"모델명: {model}")
    print(f"시스템: {args.system}")
    print(f"프롬프트: {args.prompt}")
    print(f"스트리밍: {'활성화' if stream else '비활성화'}")
    print("=" * 50)
    print()

    # 1. GET /api/tags 호출하여 서버 상태 및 모델 존재 여부 확인
    tags_url = f"{host}/api/tags"
    try:
        response = httpx.get(tags_url, timeout=10.0)
        response.raise_for_status()
        tags_data = response.json()
    except httpx.ConnectError:
        print(f"오류: Ollama 서버({host})에 연결할 수 없습니다.", file=sys.stderr)
        print("서버가 실행 중인지 확인하세요. (예: ollama serve 실행 상태 확인)", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"오류: Ollama 서버 상태를 조회하지 못했습니다. ({e})", file=sys.stderr)
        sys.exit(1)

    # 다운로드된 모델 목록 추출
    available_models = [m.get("name") for m in tags_data.get("models", [])]

    # 정확한 태그 매칭 확인
    if model not in available_models:
        print(f"오류: 지정된 모델 '{model}'이 서버에 설치되어 있지 않습니다.", file=sys.stderr)
        print(f"해결 안내:", file=sys.stderr)
        print(f"  1. 다음 터미널 명령을 실행하여 필요한 모델을 다운로드하세요:", file=sys.stderr)
        print(f"     ollama pull {model}", file=sys.stderr)
        print(f"  2. 또는 '.env' 파일의 OLLAMA_MODEL 값을 수정하거나,", file=sys.stderr)
        print(f"     실행 시 '--model' 옵션에 다운로드된 올바른 모델명을 입력하세요.", file=sys.stderr)
        print(f"\n현재 사용 가능한 모델 목록:", file=sys.stderr)
        if available_models:
            for m in available_models:
                print(f"  - {m}", file=sys.stderr)
        else:
            print(f"  (사용 가능한 모델이 없습니다. ollama pull <model> 명령으로 다운로드 받으세요.)", file=sys.stderr)
        sys.exit(1)

    # 2. 메시지 구조화 및 API 호출
    headers = {"Content-Type": "application/json"}
    messages = [
        {"role": "system", "content": args.system},
        {"role": "user", "content": args.prompt}
    ]

    try:
        if args.endpoint == "ollama":
            url = f"{host}/api/chat"
            payload = {
                "model": model,
                "messages": messages,
                "stream": stream
            }

            if stream:
                print("응답 (스트리밍): ", end="", flush=True)
                with httpx.stream("POST", url, json=payload, headers=headers, timeout=timeout) as r:
                    r.raise_for_status()
                    for line in r.iter_lines():
                        if not line.strip():
                            continue
                        data = json.loads(line)
                        content = data.get("message", {}).get("content") or ""
                        print(content, end="", flush=True)
                print()
            else:
                r = httpx.post(url, json=payload, headers=headers, timeout=timeout)
                r.raise_for_status()
                data = r.json()
                content = data.get("message", {}).get("content") or ""
                print(f"응답:\n{content}")

        elif args.endpoint == "openai":
            url = f"{host}/v1/chat/completions"
            payload = {
                "model": model,
                "messages": messages,
                "stream": stream
            }

            if stream:
                print("응답 (스트리밍): ", end="", flush=True)
                with httpx.stream("POST", url, json=payload, headers=headers, timeout=timeout) as r:
                    r.raise_for_status()
                    for line in r.iter_lines():
                        cleaned_line = line.strip()
                        if not cleaned_line:
                            continue
                        if cleaned_line.startswith("data:"):
                            data_str = cleaned_line[5:].strip()
                            if data_str == "[DONE]":
                                break
                            data = json.loads(data_str)
                            choices = data.get("choices", [])
                            if choices:
                                content = choices[0].get("delta", {}).get("content") or ""
                                print(content, end="", flush=True)
                print()
            else:
                r = httpx.post(url, json=payload, headers=headers, timeout=timeout)
                r.raise_for_status()
                data = r.json()
                choices = data.get("choices", [])
                if choices:
                    content = choices[0].get("message", {}).get("content", "")
                    print(f"응답:\n{content}")
                else:
                    print("오류: OpenAI 호환 엔드포인트에서 올바른 응답을 받지 못했습니다.", file=sys.stderr)

    except httpx.HTTPStatusError as e:
        print(f"\n오류: API 호출이 실패했습니다. (HTTP {e.response.status_code})", file=sys.stderr)
        try:
            err_data = e.response.json()
            err_msg = err_data.get("error", err_data)
            print(f"상세 에러 내용: {err_msg}", file=sys.stderr)
        except Exception:
            print(f"상세 에러 내용: {e.response.text}", file=sys.stderr)
    except Exception as e:
        print(f"\n오류: API 호출 중 예상치 못한 문제가 발생했습니다. ({e})", file=sys.stderr)

if __name__ == "__main__":
    main()
