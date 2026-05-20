# 최종 체크리스트와 문제 해결

[메인 안내로 돌아가기](../README.md)

## 행사 전 최종 체크리스트

### Windows

- PowerShell에서 `uv --version` 성공
- `uv run python --version` 성공
- PowerShell에서 `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `Invoke-RestMethod http://localhost:11434/api/tags` 성공
- 가능하면 전원 어댑터 지참하기

### Apple Silicon Mac

- `uname -m` 결과가 `arm64`
- `uv --version` 성공
- `uv run python --version` 성공
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 또는 `ollama pull gemma4:e4b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공
- 가능하면 전원 어댑터 지참하기

### Intel Mac

- `uname -m` 결과가 `x86_64`
- macOS 14 이상 확인
- `uv --version` 성공
- `uv run python --version` 성공
- `ollama --version` 성공
- `ollama pull gemma4:e2b` 완료
- `ollama run gemma4:e2b`로 1회 답변 생성 성공
- `curl http://localhost:11434/api/tags` 성공
- 큰 모델을 무리하게 받지 않기

### Google Antigravity를 사용할 경우

- Antigravity 2.0 또는 IDE를 사용할 경우 앱 실행 성공
- 사용 가능한 Google 계정 로그인 성공
- 첫 실행 설정 완료
- Antigravity 2.0을 사용할 경우 Project에 행사 자료 폴더 추가
- Antigravity IDE 또는 기존 편집기를 사용할 경우 행사 자료 폴더 열기 성공
- Antigravity CLI를 사용할 경우 `agy --version` 성공
- Antigravity CLI에서 `?`, `/usage`, `/permissions`, `/skills`, `/mcp`, `/tasks` 입력 성공
- `.agents/rules`, `.agents/workflows`, `.agents/skills` 확인
- Python 핸즈온을 진행할 경우 `hands-on/session-1/work`에서 `uv sync` 성공
- Python 핸즈온을 진행할 경우 `/session-1-01-ollama-server-api`, `/session-1-02-adk-ollama` slash command 확인

## 빠른 준비 명령 모음

Windows PowerShell:

```powershell
uv --version
uv run python --version
Set-Location hands-on/session-1/work
uv sync
Set-Location ../../..
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
Invoke-RestMethod http://localhost:11434/api/tags
```

macOS:

```bash
uv --version
uv run python --version
cd hands-on/session-1/work
uv sync
cd ../../..
ollama --version
ollama pull gemma4:e2b
ollama run gemma4:e2b
curl http://localhost:11434/api/tags
```

16GB 이상 장비에서 E4B까지 준비할 경우:

```bash
ollama pull gemma4:e4b
ollama run gemma4:e4b
```

Windows PowerShell에서도 위 두 줄을 그대로 실행하면 됩니다.

Antigravity CLI를 사용할 경우:

```bash
agy --version
agy
```

`agy` 실행 후 CLI 입력창에서 확인:

```text
?
/usage
/permissions
/skills
/mcp
/tasks
```

## 자주 생기는 문제

### `ollama` 명령을 찾을 수 없다고 나옵니다

- 터미널이나 PowerShell 창을 새로 열어 다시 실행하세요.
- macOS에서는 Ollama 앱을 한 번 실행하고 CLI 경로 연결 요청을 허용했는지 확인해 주세요.
- 그래도 안 되면 공식 설치 프로그램을 다시 실행하세요.

### `uv` 명령을 찾을 수 없다고 나옵니다

- PowerShell이나 터미널 창을 새로 열어 다시 실행하세요.
- macOS에서는 `exec $SHELL -l`을 실행한 뒤 다시 확인하세요.
- 설치가 안 되어 있으면 [Python + uv 설치 가이드](./09-python-uv-setup.md)를 따라 설치하세요.

### `uv run python --version`이 실패합니다

Python 버전 준비가 안 된 상태일 수 있습니다. [Python + uv 설치 가이드](./09-python-uv-setup.md)의 Python 설치 확인 절차를 따라 주세요.

### 모델 다운로드가 너무 오래 걸립니다

- 정상일 수 있습니다. 모델 파일은 수 GB 이상입니다.
- 행사장 네트워크에서 처음 다운로드하지 마세요.
- 일단 `gemma4:e2b`만 먼저 완료하세요.

### 실행 중 컴퓨터가 너무 느려집니다

- 더 작은 모델을 사용하세요: `gemma4:e4b` 대신 `gemma4:e2b`
- 브라우저 탭, 영상 회의 앱, 무거운 개발 도구를 닫으세요.
- 8GB 장비와 Intel Mac에서는 느릴 수 있습니다.

### API가 연결되지 않습니다

먼저 서버가 떠 있는지 확인합니다.

macOS:

```bash
curl http://localhost:11434/api/tags
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://localhost:11434/api/tags
```

실패하면 Ollama 앱을 실행하거나 `ollama serve`를 별도 터미널에서 실행하세요.

### `gemma4:latest`를 써도 되나요?

가능은 하지만 행사 준비용으로는 권장하지 않습니다. `latest`가 나중에 다른 모델로 바뀔 수 있으므로 `gemma4:e2b`, `gemma4:e4b`처럼 명시적 태그를 사용하세요.

### Google Antigravity 로그인이 안 됩니다

- Antigravity 2.0, Antigravity IDE, Antigravity CLI 모두 Google 로그인 흐름을 사용합니다.
- 회사/학교 계정이나 관리형 장비에서는 계정 정책, 설치 정책, 스크립트 실행 정책 때문에 막힐 수 있습니다.
- 행사 전에 사용할 계정으로 앱 실행, 첫 설정, 또는 `agy` 첫 실행까지 확인하세요.
- 설치가 막히면 기존 VS Code 같은 코드 편집기를 준비해도 됩니다.

### Antigravity CLI 설치나 실행이 안 됩니다

- `agy --version`이 실패하면 터미널을 새로 열고 다시 확인하세요.
- 설치 직후라면 셸 경로가 아직 반영되지 않았을 수 있습니다. macOS/Linux에서는 터미널을 새로 열거나 `exec $SHELL -l` 후 다시 확인하세요.
- 회사/학교 장비에서는 공식 설치 스크립트 실행이 차단될 수 있습니다.
- 첫 실행에서 브라우저 로그인이 열리지 않으면 CLI가 출력한 인증 URL을 직접 브라우저에 붙여넣어 진행하세요.
- Gemini CLI를 쓰던 개인 계정은 2026년 6월 18일 전환 일정을 확인하고 Antigravity CLI 설치와 로그인을 미리 끝내세요.
- CLI가 꼭 필요한 실습은 아니므로 막히면 Antigravity IDE, VS Code, AI Studio용 프롬프트 흐름으로 진행해도 됩니다.

### Antigravity workflow가 보이지 않습니다

- 저장소 루트가 아니라 하위 폴더를 연 상태인지 확인하세요.
- Antigravity 2.0에서는 Project에 저장소 루트 폴더가 추가되어 있는지 확인하세요.
- Agent 패널의 Customizations를 열고 Rules, Workflows, Skills를 확인하세요.
- 자동 인식이 안 되면 `.agents/workflows/`의 Markdown 내용을 프로젝트 또는 Workspace workflow로 직접 추가하세요.
- 자세한 설정 위치는 [Google Antigravity 2.0 및 CLI 준비 가이드](./07-google-antigravity.md)를 확인하세요.
