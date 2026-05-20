# Gemma 4 Python 핸즈온 Session 1

이 세션은 완성 코드를 따라 치는 실습이 아니라, 시스템 프롬프트로 핸즈온 코드를 단계별 생성하는 실습입니다.

## 구성

| 경로 | 용도 |
| --- | --- |
| `.agents/rules/rules.md` | Antigravity 공통 rule |
| `.agents/rules/session-1-common-rules.md` | Antigravity 수동 설정용 rule 사본 |
| `.agents/workflows/session-1-01-ollama-server-api.md` | Antigravity workflow 1 |
| `.agents/workflows/session-1-02-adk-ollama.md` | Antigravity workflow 2 |
| `.agents/skills/gemma4-python-hands-on/SKILL.md` | Antigravity skill |
| `prompts/01-ollama-server-api-system-prompt.md` | Ollama 서버 API 예제 생성용 시스템 프롬프트 |
| `prompts/02-adk-ollama-system-prompt.md` | ADK Ollama 예제 생성용 시스템 프롬프트 |
| `work/` | 생성 코드 위치와 실습용 `pyproject.toml` |
| `reference/` | 참고 구현 |

## Antigravity Skills 활용 방식

이 핸즈온에서 Antigravity의 세 가지 설정은 역할을 나누어 사용합니다.

- Rules: `hands-on/session-1/work/` 아래에 파일을 만들고, `uv run` 실행 방식을 쓰는 공통 규칙
- Workflows: `/session-1-01-ollama-server-api` 같은 slash command로 실행하는 단계별 생성 절차
- Skills: `gemma4-python-hands-on`처럼 Agent가 Session 1 Python 실습의 맥락과 검토 기준을 참고하는 작업 지식

따라서 보통 workflow를 실행하면 되고, skill은 코드 생성/검토/문제 해결의 품질을 맞추는 보조 장치로 사용합니다.

```text
/session-1-01-ollama-server-api
시작
```

skill이 자동으로 참고되지 않는 것처럼 보이면 Agent 요청에 skill 이름을 직접 넣습니다.

```text
gemma4-python-hands-on skill을 참고해서 Session 1 규칙에 맞게 코드를 생성해 줘.
```

생성된 코드가 reference와 크게 다르거나 실행이 실패하면 skill 기준으로 다시 검토하게 합니다.

```text
gemma4-python-hands-on skill 기준으로 hands-on/session-1/work/01_ollama_server_api.py를 검토하고 필요한 부분만 고쳐 줘.
```

## 진행 시간

| 시간 | 내용 |
| ---: | --- |
| 0-5분 | `uv`, Python, Ollama 준비 확인 |
| 5-10분 | `work/pyproject.toml` 확인과 `uv sync` |
| 10-30분 | 01 프롬프트로 Ollama 서버 API 코드 생성과 실행 |
| 30-55분 | 02 프롬프트로 ADK Ollama agent 생성과 실행 |
| 55-60분 | 직접 API 호출과 ADK agent 호출 차이 정리 |

## 0. 사전 준비

Python, `uv`, Ollama를 확인합니다. `uv`가 설치되어 있지 않다면 먼저 [Python + uv 설치 가이드](../../docs/09-python-uv-setup.md)를 확인하세요.

```bash
uv --version
uv run python --version
ollama --version
```

Ollama 실습 전에는 모델이 미리 다운로드되어 있어야 합니다.

```bash
ollama pull gemma4:e2b
ollama list
```

16GB 이상 장비에서는 `gemma4:e4b`도 사용할 수 있습니다.

macOS/Linux:

```bash
ollama pull gemma4:e4b
export OLLAMA_MODEL=gemma4:e4b
```

Windows PowerShell:

```powershell
ollama pull gemma4:e4b
$env:OLLAMA_MODEL = "gemma4:e4b"
```

## 1. uv 프로젝트 확인

`work/` 폴더에는 실습용 `pyproject.toml`이 이미 들어 있습니다. `uv init`이나 `uv add`를 다시 실행할 필요는 없습니다.

```bash
cd hands-on/session-1/work
uv sync
```

`uv sync`는 로컬 `.venv/`를 만들고 필요한 패키지를 설치합니다. 실습 중 `uv run ...`을 처음 실행해도 같은 프로젝트 설정을 기준으로 환경이 준비됩니다.

의존성 역할:

- `google-adk`: ADK agent 정의와 실행
- `python-dotenv`: `.env` 파일에서 로컬 서버 설정 로드
- `httpx`: Ollama 서버 API 호출과 ADK Ollama custom adapter 구현

## 2. 01 Ollama 서버 API 코드 생성

Antigravity를 사용하는 경우 Agent 채팅에서 workflow를 호출합니다.

```text
/session-1-01-ollama-server-api
시작
```

AI Studio 또는 다른 도구를 사용하는 경우 System Instructions에 다음 파일 전체를 넣습니다.

```text
hands-on/session-1/prompts/01-ollama-server-api-system-prompt.md
```

일반 프롬프트에는 이렇게 입력합니다.

```text
시작
```

AI Studio는 로컬 파일을 직접 만들지 못하므로, 응답에 나온 코드 블록을 아래 경로에 직접 저장합니다.

```text
hands-on/session-1/work/01_ollama_server_api.py
hands-on/session-1/work/.env.example
```

## 3. .env 파일 준비

생성된 `.env.example`을 `.env`로 복사하고 로컬 Ollama 설정을 확인합니다.

macOS/Linux:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

`.env` 예시:

```dotenv
OLLAMA_HOST=http://localhost:11434
OLLAMA_API_BASE=http://localhost:11434
OLLAMA_MODEL=gemma4:e2b
ADK_OLLAMA_MODEL=gemma4:e2b
```

## 4. 01 Ollama 서버 API 코드 실행

Ollama 앱을 켜거나 별도 터미널에서 서버를 실행합니다.

```bash
ollama serve
```

서버 확인:

```bash
curl http://localhost:11434/api/tags
```

Ollama native API:

```bash
uv run python -m py_compile 01_ollama_server_api.py
uv run python 01_ollama_server_api.py --help
uv run python 01_ollama_server_api.py
```

OpenAI 호환 API:

```bash
uv run python 01_ollama_server_api.py --endpoint openai
```

## 5. 02 ADK Ollama Agent 생성

01에서 Ollama 서버 API를 직접 호출했다면, 이번에는 ADK agent가 작은 custom model adapter를 통해 로컬 Ollama Gemma 4를 쓰도록 만듭니다. 이 실습에서는 Ollama `/api/chat`을 직접 호출합니다.

Antigravity를 사용하는 경우:

```text
/session-1-02-adk-ollama
시작
```

AI Studio 또는 다른 도구를 사용하는 경우 System Instructions에 다음 파일 전체를 넣습니다.

```text
hands-on/session-1/prompts/02-adk-ollama-system-prompt.md
```

일반 프롬프트:

```text
시작
```

AI Studio 응답에 나온 코드 블록을 아래 경로에 저장합니다.

```text
hands-on/session-1/work/adk_02_ollama_agent/__init__.py
hands-on/session-1/work/adk_02_ollama_agent/agent.py
```

## 6. 02 ADK Ollama Agent 실행

Ollama 서버를 켠 뒤 `OLLAMA_API_BASE`를 확인합니다.

macOS/Linux:

```bash
export OLLAMA_API_BASE="${OLLAMA_HOST:-http://localhost:11434}"
```

Windows PowerShell:

```powershell
$env:OLLAMA_API_BASE = "http://localhost:11434"
```

실행:

```bash
uv run python -m py_compile adk_02_ollama_agent/agent.py
uv run adk run adk_02_ollama_agent
```

예시 입력:

```text
MongoDB 벡터 검색을 로컬 Gemma 4와 함께 쓰는 흐름을 3단계로 설명해 줘.
```

종료는 터미널에서 `Ctrl+C`를 누릅니다.

## 참고 구현

`reference/`에는 각 프롬프트가 만들도록 의도한 최소 구현이 들어 있습니다. 생성 결과가 크게 벗어났을 때 비교용으로 사용하세요.

## Antigravity 수동 설정

Antigravity가 `.agents/` 설정을 자동으로 인식하지 못하는 경우에는 UI에서 직접 추가합니다.

Rules:

```text
.agents/rules/rules.md
.agents/rules/session-1-common-rules.md
```

Workflows:

```text
.agents/workflows/session-1-01-ollama-server-api.md
.agents/workflows/session-1-02-adk-ollama.md
```

Skills:

```text
.agents/skills/gemma4-python-hands-on/SKILL.md
```

수동 추가 후에는 새 Agent 대화를 열거나 workspace를 다시 열어 rules, workflows, skills가 반영됐는지 확인하세요.
