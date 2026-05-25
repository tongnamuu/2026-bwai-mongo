# [MUG Seoul x GDG Korea] 하루 만에 끝내는 로컬 RAG 프로토타이핑

MongoDB User Group(MUG) Seoul과 Google Developer Groups(GDG) Korea가 함께하는 이번 커뮤니티 이벤트는 두 생태계가 만나 각 기술이 어떻게 연결되고 서로를 보완하는지 함께 탐색하는 자리입니다.

본격적인 클라우드 배포에 앞서, 로컬 환경에서 빠르게 RAG 시스템을 프로토타이핑해 보고 싶은 개발자분들을 위한 핸즈온 세션입니다. Gemma 4, voyage-4-nano 임베딩, 그리고 MongoDB를 활용해 처음부터 끝까지 로컬에서 동작하는 RAG 파이프라인을 직접 구축해 봅니다.

신청: https://www.meetup.com/mongodb-usergroup-seoul/events/314765122/

기준 확인일: 2026-05-17

---

## 세션 구성

| 세션 | 주제 | 사전 준비 | 현장 실습 |
|---|---|---|---|
| Session 1 | Gemma 4 Python 핸즈온: Ollama 서버 API와 ADK 연동 | [→ 사전 준비](hands-on/session-1/prerequisites.md) | [→ 핸즈온 가이드](hands-on/session-1/README.md) |
| Session 2 | 로컬 RAG 파이프라인: MongoDB Vector Search + voyage-4-nano | [→ 사전 준비](hands-on/session-2/prerequisites.md) | [→ 핸즈온 가이드](hands-on/session-2/README.md) |

---

## 행사 전 설치/다운로드 요약

현장 네트워크에서 모델, Docker 이미지, Python 패키지를 처음 다운로드하면 실습 시간이 크게 줄어들 수 있습니다. 행사 전에 아래 항목을 미리 준비해 주세요.

| 구분 | 준비 항목 | 대상 | 비고 |
|---|---|---|---|
| 공통 필수 | Python + `uv` | Session 1, 2 | [Python + uv 설치 가이드](docs/09-python-uv-setup.md) |
| 공통 필수 | Ollama | Session 1, 2 | [Ollama와 Gemma 4 개요](docs/01-ollama-gemma4-overview.md) |
| 공통 필수 | `gemma4:e4b` | Session 1, 2 | 기본 Gemma 4 모델 |
| 저사양 대체 | `gemma4:e2b` | 8GB 메모리 장비 | 8GB 노트북만 사용 |
| Session 2 필수 | Docker Desktop | Session 2 | Local Atlas 실행에 필요 |
| Session 2 권장 | Atlas CLI + Local Atlas 초기 구동 | Session 2 | Docker 이미지 사전 다운로드 목적 |
| Session 2 권장 | Python 패키지 설치 (`uv sync`) | Session 2 | 노트북 실행 환경 준비 |
| Session 2 권장 | `voyageai/voyage-4-nano` | Session 2 | 로컬 임베딩 모델, HuggingFace에서 최초 1회 다운로드 |
| Session 2 필수 | Jupyter 노트북 실행 환경 | Session 2 | Antigravity IDE, VS Code, 또는 Jupyter Lab |
| 선택 | Antigravity IDE 또는 CLI(`agy`) | Session 1 중심 | 에이전트 기반 코드 생성 흐름을 따라갈 경우 |

모델 다운로드:

```bash
ollama pull gemma4:e4b
```

8GB 메모리 장비만:

```bash
ollama pull gemma4:e2b
```

Session 2 임베딩 모델 사전 다운로드:

```bash
cd hands-on/session-2/work
uv sync
uv run python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('voyageai/voyage-4-nano', trust_remote_code=True); print('voyage-4-nano cached')"
```

Session 2 Local Atlas 이미지 사전 다운로드:

```bash
atlas local setup local-rag
```

---

## Session 1 — Gemma 4 Python 핸즈온

Ollama로 로컬에 내려받은 Gemma 4를 Ollama 서버 API와 ADK agent로 각각 연동하는 Python 코드를 생성하고 실행합니다. 코드를 미리 작성해 두는 실습이 아니라, 핸즈온 현장에서 시스템 프롬프트로 코드를 직접 생성하는 방식으로 진행됩니다.

**행사 전에 준비해야 할 것:** Ollama 설치 + Gemma 4 모델 다운로드 + Python + `uv`

**에이전트 기반 코드 생성을 함께 진행할 경우:** Antigravity IDE 또는 Antigravity CLI(`agy`)

Gemma 4 모델은 수 GB이므로 현장 네트워크 상태에 따라 다운로드 시간이 크게 달라질 수 있습니다. 반드시 행사 전에 완료하세요.

→ **[Session 1 사전 준비 가이드](hands-on/session-1/prerequisites.md)**

---

## Session 2 — 로컬 RAG 파이프라인

MongoDB Local Atlas, voyage-4-nano 임베딩 모델(로컬 실행), Ollama Gemma 4를 조합해 외부 API 키 없이 완전히 로컬에서 동작하는 RAG 파이프라인을 노트북 하나로 구축합니다.

**행사 전에 준비해야 할 것:** Docker 설치(필수) + Atlas CLI 설치 및 Local Atlas 초기 구동(권장) + Python 패키지/`voyageai/voyage-4-nano` 사전 다운로드(권장) + Jupyter 노트북 실행 환경

Atlas CLI로 Local Atlas Docker 이미지를 미리 받아두고, HuggingFace 임베딩 모델 캐시까지 받아두면 현장에서 기다림 없이 바로 시작할 수 있습니다.

→ **[Session 2 사전 준비 가이드](hands-on/session-2/prerequisites.md)**
