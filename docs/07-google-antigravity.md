# Google Antigravity 2.0 및 CLI 준비 가이드

[메인 안내로 돌아가기](../README.md)

## 이 문서는 언제 보면 되나요?

- 행사 중 코드를 직접 열어보고 수정할 가능성이 있을 때
- 기존 VS Code 대신 Antigravity IDE를 써 보고 싶을 때
- Antigravity 2.0의 에이전트 중심 작업 환경을 미리 설치해 보고 싶을 때
- Antigravity CLI를 터미널에서 써 보고 싶을 때
- Gemini CLI를 쓰고 있어서 Antigravity CLI 전환 일정을 확인해야 할 때

Ollama와 Gemma 4 실행 자체에는 Antigravity가 필수는 아닙니다. 코드 편집기가 이미 준비되어 있다면 기존 편집기를 사용해도 됩니다.

## Google Antigravity란 무엇인가요?

Google Antigravity는 Google의 agent-first 개발 플랫폼입니다. Google I/O 2026 발표 기준으로 Antigravity는 IDE 하나를 뜻하는 이름이 아니라, 데스크톱 앱, IDE, CLI가 나뉘어 있는 제품군으로 이해하는 편이 정확합니다.

### 용어 정리

- Antigravity 2.0: IDE와 분리된 독립 데스크톱 앱입니다. Project 단위로 여러 폴더를 묶고, 에이전트를 동기/비동기로 실행하며, 결과물과 권한을 관리합니다.
- Antigravity IDE: 코드 편집기형 앱입니다. 실습 중 파일을 직접 열어 수정하거나 Jupyter 같은 편집기 확장이 필요하면 Antigravity IDE 또는 기존 VS Code를 사용합니다.
- Antigravity CLI, AGY CLI: 터미널에서 `agy` 명령으로 실행하는 Antigravity 터미널 UI입니다. Antigravity 2.0과 같은 agent harness와 주요 설정을 공유합니다.
- Project: Antigravity 2.0에서 에이전트 대화와 권한의 경계가 되는 단위입니다. 하나의 Project에 여러 폴더나 저장소를 연결할 수 있습니다.
- Rules, Workflows, Skills: 이 저장소의 `.agents/` 아래에 둔 에이전트 커스터마이징 파일입니다. Rules는 지속 규칙, Workflows는 반복 실행 절차, Skills는 작업별 지식과 절차입니다.
- Plugins: Antigravity CLI에서 skills, agents, rules, MCP 서버, hooks 등을 묶어 배포하는 단위입니다.

### Antigravity CLI를 쓰면 좋은 경우

공식 문서는 Antigravity CLI를 Antigravity의 가벼운 Terminal User Interface로 설명합니다. 같은 에이전트 기능을 터미널에서 쓰기 위한 표면이므로, 다음 상황에 잘 맞습니다.

- 키보드 중심으로 작업하고 싶을 때
- 원격 SSH 환경에서 에이전트를 실행해야 할 때
- IDE보다 가벼운 실행 환경이 필요할 때
- `uv`, `ollama`, `git` 같은 터미널 명령과 에이전트 작업을 한 흐름에서 다루고 싶을 때

Antigravity CLI와 Antigravity 2.0은 같은 agent harness를 사용하고, 핵심 설정과 권한 설정을 공유합니다. 다만 대화 기록은 기본적으로 별개로 관리되므로, 행사 준비에서는 CLI와 데스크톱 앱 중 실제로 사용할 환경 하나를 먼저 안정적으로 준비하는 것을 권장합니다.

## Antigravity 2.0 또는 IDE 공통 준비

1. 공식 다운로드 페이지로 이동합니다.

```text
https://antigravity.google/download
```

2. 본인 운영체제에 맞는 설치 파일을 다운로드합니다.
3. 설치 후 앱을 실행합니다.
4. 첫 실행 설정을 완료합니다.
5. 사용 가능한 Google 계정으로 로그인할 수 있는지 확인합니다.
6. Antigravity 2.0을 사용할 경우 Project를 만들고 행사 자료 폴더를 추가합니다.
7. Antigravity IDE 또는 기존 편집기를 사용할 경우 행사 자료 폴더를 열 수 있는지 확인합니다.

## Windows 설치

1. https://antigravity.google/download 로 이동합니다.
2. Windows용 설치 파일을 다운로드합니다.
3. 다운로드한 설치 프로그램을 실행합니다.
4. 설치가 끝나면 Antigravity를 실행합니다.
5. 첫 실행 화면에서 설정을 진행합니다.
6. 사용 가능한 Google 계정으로 로그인합니다.
7. Antigravity 2.0에서는 Project에 행사 자료 폴더를 추가하고, IDE에서는 행사 자료 폴더를 열어 봅니다.

회사/학교 장비에서는 설치 프로그램 실행이나 로그인 단계가 보안 정책으로 막힐 수 있습니다. 이 경우 행사 전에 관리자 권한 또는 다른 개인 장비를 확인해 주세요.

## macOS Apple Silicon 설치

1. https://antigravity.google/download 로 이동합니다.
2. Apple Silicon Mac에 맞는 macOS 설치 파일을 다운로드합니다.
3. 다운로드한 DMG 파일을 엽니다.
4. Antigravity 앱을 `Applications` 폴더로 옮깁니다.
5. `Applications` 폴더에서 Antigravity를 실행합니다.
6. macOS 보안 확인 창이 나오면 신뢰할 수 있는 공식 다운로드인지 확인한 뒤 열기를 진행합니다.
7. 사용 가능한 Google 계정으로 로그인합니다.
8. Antigravity 2.0에서는 Project에 행사 자료 폴더를 추가하고, IDE에서는 행사 자료 폴더를 열어 봅니다.

## macOS Intel Mac 설치

Antigravity 2.0 데스크톱 앱은 공식 다운로드 페이지의 최소 요구 사항에서 macOS x86 미지원으로 표시됩니다. Intel Mac 사용자는 Antigravity IDE 또는 기존 VS Code 같은 코드 편집기를 준비하세요.

Intel Mac에서는 Ollama/Gemma 4 실행도 CPU 전용이라 느릴 수 있습니다. 메모리가 8GB라면 Ollama 실행과 편집기를 동시에 켰을 때 전체 시스템이 느려질 수 있으니 `gemma4:e2b`와 가벼운 편집기 조합을 권장합니다.

## Linux 설치

Antigravity 2.0은 공식 다운로드 기준으로 Linux도 지원합니다. 다만 이 행사 사전 준비 문서의 Ollama/Gemma 4 로컬 실행 절차는 Windows와 macOS만 다룹니다. Linux 사용자는 Antigravity 설치는 공식 다운로드 페이지를 따르고, 로컬 모델 실행은 각자 환경에서 사전 테스트를 마쳐 주세요.

## Antigravity CLI 설치

Antigravity CLI는 `agy` 명령으로 실행하는 터미널 UI입니다. 설치 스크립트는 공식 Antigravity 도메인에서 내려받아 실행하므로, 회사/학교 장비에서는 보안 정책에 막힐 수 있습니다.

가능하면 Antigravity 2.0 또는 Antigravity IDE에서 먼저 로그인한 뒤 CLI를 실행하세요. 저장된 로그인 세션이 있으면 CLI가 운영체제의 보안 keyring을 통해 조용히 인증을 시도하고, 세션이 없으면 브라우저 기반 Google 로그인으로 넘어갑니다.

이미 설치되어 있다면 새로 설치하지 말고 버전 확인부터 진행하세요.

```bash
agy --version
```

Mac/Linux:

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
agy --version
agy
```

Windows PowerShell:

```powershell
irm https://antigravity.google/cli/install.ps1 | iex
agy --version
agy
```

Windows CMD:

```cmd
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
agy --version
agy
```

원격 SSH 환경에서는 CLI가 인증 URL을 출력합니다. 이 URL을 로컬 브라우저에 붙여넣어 로그인한 뒤, 발급된 인증 코드를 터미널에 붙여넣으면 됩니다. 로그아웃이 필요하면 CLI 입력창에서 `/logout`을 실행하세요.

## Antigravity CLI 기본 사용법

Antigravity CLI는 작업할 폴더에서 `agy`를 실행해 시작합니다. 행사 자료 저장소 루트에서 시작해야 `.agents/` 설정과 실습 파일을 함께 찾기 쉽습니다.

```bash
cd <행사-자료-저장소-루트>
agy
```

처음 실행하면 Google 로그인 또는 온보딩 화면이 나올 수 있습니다. 로그인이 끝나면 아래 명령을 CLI 입력창에 직접 입력해 기본 기능을 확인합니다.

```text
?
/usage
/permissions
/skills
/mcp
/tasks
```

행사 전에는 다음 테스트 프롬프트를 한 번 실행해 보세요. 파일 수정 없이 읽기만 시키는 확인용 요청입니다.

```text
현재 폴더의 파일 구성을 읽고 Session 1 사전 준비에서 확인해야 할 항목만 요약해 줘. 파일은 수정하지 마.
```

### 자주 쓰는 CLI 입력

| 입력 | 용도 |
| --- | --- |
| `?` 또는 `/usage` | 도움말과 slash command 목록 확인 |
| `/permissions` | 에이전트 자율성 수준 선택: `request-review`, `always-proceed`, `strict` |
| `/config` 또는 `/settings` | CLI 설정 화면 열기 |
| `/model` | 기본 reasoning model 선택 |
| `/keybindings` | 키보드 단축키 편집 |
| `/skills` | 로컬/글로벌 skill 목록 확인 |
| `/mcp` | MCP 서버 설정 확인 |
| `/tasks` | 백그라운드 작업 상태 확인 |
| `/agents` | 실행 중인 subagent 상태 확인 |
| `/resume` | 이전 대화 다시 열기 |
| `/rewind` 또는 `/undo` | 대화 기록을 이전 지점으로 되돌리기 |
| `/open <path>` | 외부 편집기로 파일 열기 |
| `/logout` | 저장된 Google 로그인 세션 제거 |
| `@` | 파일 경로 자동완성 |
| `!<명령>` | 터미널 명령 실행 요청 |

권한 요청이 나오면 내용을 읽고 승인하세요. 실습 전에는 기본 권한 설정을 유지하고, 에이전트가 파일을 수정하거나 명령을 실행하려 할 때 어떤 작업인지 확인하는 흐름을 권장합니다. 참가자 안내에서는 위험한 권한 우회 옵션을 사용하지 마세요.

### 설정 파일 위치

Antigravity CLI 설정은 사용자 홈 디렉터리에 저장됩니다. 행사 자료 저장소에는 개인 설정 파일을 커밋하지 않습니다.

```text
~/.gemini/antigravity-cli/settings.json
~/.gemini/antigravity-cli/keybindings.json
~/.gemini/antigravity-cli/plugins/<plugin_name>/
```

터미널 sandbox 같은 실행 안전 설정도 `settings.json` 또는 `/config`에서 조정할 수 있습니다. 행사 준비 단계에서는 기본값을 유지하고, 명령 실행 요청이 나올 때마다 내용을 확인하는 방식을 권장합니다.

## 첫 실행 설정

첫 실행에서는 다음 항목이 나올 수 있습니다.

- 기존 VS Code 또는 Cursor 설정 가져오기
- 새 설정으로 시작하기
- 편집기 테마 선택
- Agent 사용 방식 설정
- 확장 프로그램 설치 여부 선택
- Antigravity 2.0 Project 생성 또는 폴더 추가
- Antigravity IDE를 계속 둘지 여부 선택

처음 준비하는 경우에는 새 설정으로 시작해도 됩니다. 이미 VS Code 설정을 많이 쓰고 있다면 가져오기를 선택해도 됩니다. Antigravity 2.0은 IDE가 아니므로, 편집기 기능이 필요하면 Antigravity IDE 또는 기존 편집기를 함께 준비하세요.

## Rules, Workflows, Skills 설정

이 저장소를 Antigravity에서 열면 행사 실습용 설정을 함께 사용할 수 있습니다. 저장소 루트가 아니라 하위 폴더만 열면 `.agents/` 설정을 못 찾을 수 있으니, 가능하면 이 저장소 루트를 그대로 여세요. Antigravity 2.0에서는 이 저장소 루트를 Project에 폴더로 추가하면 됩니다.

```text
.agents/
├── rules/
├── workflows/
└── skills/
```

Rules와 Workflows는 Agent 패널의 Customizations 화면에서 확인하거나 추가할 수 있습니다. 이 저장소의 파일이 자동으로 보이지 않으면 같은 화면에서 프로젝트 또는 Workspace 항목으로 직접 추가하세요.

### Rules

Rules는 Agent가 계속 따라야 하는 제약과 코딩 스타일을 적어 두는 파일입니다.

이번 실습에서는 다음 파일을 사용합니다.

```text
.agents/rules/rules.md
.agents/rules/session-1-common-rules.md
```

`rules.md`는 항상 적용할 공통 rule이고, `session-1-common-rules.md`는 UI에서 직접 붙여넣어야 할 때 쓰기 쉬운 사본입니다.

이 저장소에서는 Antigravity 설정 기본 위치로 `.agents/rules`를 사용합니다. 이전 `.agent/rules`를 쓰던 자료와 섞이지 않도록 행사 자료에서는 `.agents/`만 기준으로 봅니다.

모든 workspace에 적용할 개인 규칙은 global rule로 둘 수 있습니다.

```text
~/.gemini/GEMINI.md
```

Rule 활성화 방식은 다음 중 하나를 고를 수 있습니다.

- Manual: Agent 입력창에서 직접 언급했을 때만 사용
- Always On: 항상 적용
- Model Decision: 설명을 보고 모델이 적용 여부 판단
- Glob: `*.py`, `src/**/*.ts` 같은 파일 패턴에 맞을 때 적용

Rules 파일 하나는 12,000자 이내로 유지하세요. 다른 파일을 참고해야 하면 rule 파일 안에서 `@filename` 형태로 연결할 수 있습니다.

### Workflows

Workflows는 반복 작업 절차를 Markdown으로 저장해 두고 Agent 입력창에서 slash command로 실행하는 기능입니다.

이번 실습에서는 `.agents/workflows/` 아래의 Session 1 workflow를 사용합니다.

```text
.agents/workflows/session-1-01-ollama-server-api.md
.agents/workflows/session-1-02-adk-ollama.md
```

Agent 입력창에서는 파일명에서 `.md`를 뺀 이름으로 실행합니다.

```text
/session-1-01-ollama-server-api
/session-1-02-adk-ollama
```

Workflow가 보이지 않으면 Customizations 패널의 Workflows에서 프로젝트 또는 Workspace workflow로 직접 추가하고, 파일 내용을 붙여넣으면 됩니다.

Workflow 파일도 12,000자 이내로 유지하세요. 여러 반복 절차가 필요하면 하나의 긴 workflow보다 목적별 workflow로 나누는 편이 좋습니다.

### Skills

Skills는 특정 작업을 잘 처리하기 위한 지식과 절차를 묶어 둔 폴더입니다. 이 저장소의 skill은 다음 위치에 둡니다.

```text
.agents/skills/<skill-name>/SKILL.md
```

이 저장소에는 Session 1 Python 핸즈온을 위한 skill이 포함되어 있습니다.

```text
.agents/skills/gemma4-python-hands-on/SKILL.md
```

`SKILL.md`에는 YAML frontmatter가 필요합니다. `description`은 필수이며, Agent가 어떤 상황에서 skill을 읽을지 판단하는 힌트가 됩니다.

```markdown
---
name: my-skill
description: Helps with a specific task.
---

# My Skill

Instructions for the agent go here.
```

Global skill은 여러 작업 공간에서 쓸 수 있지만, 행사 실습에서는 프로젝트별 동작을 맞추기 위해 저장소 안의 skill을 권장합니다.

```text
~/.gemini/antigravity/skills/<skill-name>/
```

Antigravity CLI의 개인 설정, 단축키, plugin 파일은 사용자 홈 디렉터리의 `~/.gemini/antigravity-cli/` 아래에 저장됩니다. 행사 자료 저장소 안에는 넣지 않습니다.

### 설정 시 주의사항

- 실제 API 키, 토큰, 비밀번호를 rules, workflows, skills에 넣지 마세요.
- 참가자마다 다른 로컬 경로나 계정 정보는 문서에 고정하지 마세요.
- 실습 중 반복할 절차는 workflow에, 장기적으로 지켜야 할 규칙은 rule에, 특정 작업 지식은 skill에 두세요.
- 설정을 수정한 뒤에는 새 Agent 대화를 열거나 Project 또는 workspace를 다시 열어 반영 여부를 확인하세요.

## Gemini CLI에서 Antigravity CLI로 전환

2026년 5월 19일 발표 기준으로 Antigravity CLI는 모두에게 제공됩니다. 개인 사용자 중 Google AI Pro/Ultra 또는 무료 Gemini Code Assist for individuals 경로를 쓰는 경우, 2026년 6월 18일부터 Gemini CLI와 Gemini Code Assist IDE 확장이 요청을 처리하지 않습니다. Gemini Code Assist Standard/Enterprise나 Google Cloud 기반 엔터프라이즈 사용자는 별도 정책이 적용되므로 조직 안내를 따르세요.

Gemini CLI를 이미 쓰고 있다면 행사 전에 다음을 확인하세요.

- Antigravity CLI 설치와 `agy --version` 확인
- 첫 `agy` 실행과 Google 로그인 확인
- 기존 Gemini CLI skills, MCP 서버, 설정을 가져올지 여부 확인
- CLI 안에서 `?`, `/usage`, `/permissions`, `/skills`, `/mcp`, `/tasks` 같은 기본 slash command가 열리는지 확인

## 행사 전 확인

- Antigravity 2.0 또는 IDE를 사용할 경우 앱 실행 성공
- 사용 가능한 Google 계정 로그인 성공
- 첫 실행 설정 완료
- Antigravity 2.0을 사용할 경우 Project에 행사 자료 폴더 추가
- Antigravity IDE 또는 기존 편집기를 사용할 경우 행사 자료 폴더 열기 성공
- Antigravity CLI를 사용할 경우 `agy --version` 성공
- Antigravity CLI를 사용할 경우 `?`, `/usage`, `/permissions`, `/skills`, `/mcp`, `/tasks` 입력 성공
- `.agents/rules`, `.agents/workflows`, `.agents/skills` 인식 확인
- Python 핸즈온 workflow slash command 확인

Antigravity 설치나 로그인이 어렵다면 기존 VS Code 같은 코드 편집기를 준비해도 됩니다. 이 문서의 핵심 준비는 Ollama 설치, Gemma 4 모델 다운로드, API 테스트입니다.

## 공식 참고 링크

- Google Antigravity 다운로드: https://antigravity.google/download
- Introducing Google Antigravity 2.0: https://antigravity.google/blog/introducing-google-antigravity-2-0
- Google Antigravity CLI: https://antigravity.google/blog/introducing-google-antigravity-cli
- Gemini CLI에서 Antigravity CLI로 전환 안내: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/
- Antigravity 2.0 Overview: https://antigravity.google/docs/overview
- Antigravity CLI Overview: https://antigravity.google/docs/cli-overview
- Antigravity CLI Getting Started: https://antigravity.google/docs/cli-getting-started
- Antigravity CLI Using AGY CLI: https://antigravity.google/docs/cli-using
- Antigravity CLI Features: https://antigravity.google/docs/cli-features
- Google Antigravity Rules / Workflows: https://antigravity.google/docs/rules-workflows
- Google Antigravity Skills: https://antigravity.google/docs/skills
