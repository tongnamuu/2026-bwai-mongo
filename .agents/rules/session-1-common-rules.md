# Session 1 Common Rules

이 워크스페이스는 Gemma 4 Python 핸즈온 실습용입니다.

항상 다음 규칙을 지키세요.

- 모든 참가자 생성 파일은 `hands-on/session-1/work/` 아래에 둡니다.
- Python 3.10 이상 기준으로 작성합니다.
- `uv` 프로젝트 방식으로 작성합니다.
- Python 파일에 PEP 723 inline script metadata를 넣지 않습니다.
- 일반 Python 스크립트 실행 명령은 `uv run python <file>` 형식을 사용합니다.
- ADK agent 실행 명령은 `uv run adk run <agent_package>` 형식을 사용합니다.
- API 키와 설정은 `.env` 파일에서 `python-dotenv`로 읽습니다.
- 실제 API 키가 들어간 `.env` 파일을 만들거나 출력하지 않습니다.
- 공유 가능한 예시는 `.env.example`에만 작성합니다.
- Gemini API 호출은 `google-genai`를 사용합니다.
- Ollama 서버 API 호출은 `httpx`를 사용합니다.
- ADK agent는 `google-adk`를 사용하고 모듈 최상위에 `root_agent`를 정의합니다.
- ADK로 Gemini API를 호출할 때는 `google.adk.models.Gemini`를 사용합니다.
- ADK로 Ollama를 호출할 때는 `BaseLlm` 기반의 작은 custom adapter를 만들고 `httpx`로 Ollama `/api/chat`을 직접 호출합니다.
- ADK Ollama agent에서는 `OLLAMA_API_BASE`를 우선 사용하고, 없으면 `OLLAMA_HOST` 또는 `http://localhost:11434`를 사용합니다.
- ADK Ollama agent에는 외부 모델 라우팅 라이브러리나 별도 모델 래퍼를 추가하지 않습니다.
- 코드는 초보자가 읽을 수 있게 짧고 명확하게 작성합니다.
- 오류 메시지는 한국어로 작성합니다.
- 생성 후 가능한 경우 `py_compile`과, 일반 Python 스크립트라면 `--help` 실행으로 확인합니다.
- 사용자가 명시적으로 요청하기 전에는 실제 Gemini API 호출이나 긴 Ollama 생성 호출을 실행하지 않습니다.
