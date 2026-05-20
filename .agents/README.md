# Antigravity Rules, Workflows, and Skills

이 폴더는 Google Antigravity에서 workspace rules, workflows, skills로 사용할 참가자용 설정입니다.

## Rules

- `rules/rules.md`: Antigravity가 항상 적용할 workspace rule
- `rules/session-1-common-rules.md`: Session 1 공통 규칙의 수동 설정용 사본

## Workflows

- `workflows/session-1-01-ollama-server-api.md`: Ollama 로컬 서버 API 호출 코드 생성
- `workflows/session-1-02-adk-ollama.md`: ADK agent로 Ollama 로컬 Gemma 4 호출 코드 생성

## Skills

- `skills/gemma4-python-hands-on/SKILL.md`: Session 1 Python 핸즈온 생성과 검토에 사용할 작업 지식

Workflow는 slash command로 실행하고, skill은 Agent가 작업 맥락과 검토 기준을 참고하도록 돕는 용도로 사용합니다. Skill이 자동으로 적용되지 않는 것처럼 보이면 Agent 요청에 `gemma4-python-hands-on skill을 참고해서`라고 직접 적어 주세요.

Antigravity에서 이 저장소 루트를 열면 workspace 설정으로 사용할 수 있습니다. UI에서 직접 만들 경우에는 위 파일 내용을 각각 Rules, Workflows, Skills에 붙여넣으면 됩니다.
