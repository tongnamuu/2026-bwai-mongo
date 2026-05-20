# [MUG Seoul x GDG Korea] 하루 만에 끝내는 로컬 RAG 프로토타이핑

MongoDB User Group(MUG) Seoul과 Google Developer Groups(GDG) Korea가 함께하는 이번 커뮤니티 이벤트는 두 생태계가 만나 각 기술이 어떻게 연결되고 서로를 보완하는지 함께 탐색하는 자리입니다.

본격적인 클라우드 배포에 앞서, 로컬 환경에서 빠르게 RAG 시스템을 프로토타이핑해 보고 싶은 개발자분들을 위한 핸즈온 세션입니다. Gemma 4, voyage-4-nano 임베딩, 그리고 MongoDB를 활용해 처음부터 끝까지 로컬에서 동작하는 RAG 파이프라인을 직접 구축해 봅니다.

신청: https://www.meetup.com/mongodb-usergroup-seoul/events/314765122/

기준 확인일: 2026-05-17

---

## 세션 구성

| 세션 | 주제 | 사전 준비 | 현장 실습 |
|---|---|---|---|
| Session 1 | Gemma 4 Python 핸즈온: Gemini API, ADK, Ollama 연동 | [→ 사전 준비](hands-on/session-1/prerequisites.md) | [→ 핸즈온 가이드](hands-on/session-1/README.md) |
| Session 2 | 로컬 RAG 파이프라인: MongoDB Vector Search + voyage-4-nano | [→ 사전 준비](hands-on/session-2/prerequisites.md) | [→ 핸즈온 가이드](hands-on/session-2/README.md) |

---

## Session 1 — Gemma 4 Python 핸즈온

Ollama로 로컬에 내려받은 Gemma 4를 Gemini API, ADK, Ollama 서버 API로 각각 연동하는 Python 코드를 생성하고 실행합니다. 코드를 미리 작성해 두는 실습이 아니라, 핸즈온 현장에서 시스템 프롬프트로 코드를 직접 생성하는 방식으로 진행됩니다.

**행사 전에 준비해야 할 것:** Ollama 설치 + Gemma 4 모델 다운로드 + Python + `uv`

Gemma 4 모델은 수 GB이므로 현장 네트워크 상태에 따라 다운로드 시간이 크게 달라질 수 있습니다. 반드시 행사 전에 완료하세요.

→ **[Session 1 사전 준비 가이드](hands-on/session-1/prerequisites.md)**

---

## Session 2 — 로컬 RAG 파이프라인

MongoDB Local Atlas, voyage-4-nano 임베딩 모델(로컬 실행), Ollama Gemma 4를 조합해 외부 API 키 없이 완전히 로컬에서 동작하는 RAG 파이프라인을 노트북 하나로 구축합니다.

**행사 전에 준비해야 할 것:** Docker 설치(필수) + Atlas CLI 설치 및 Local Atlas 초기 구동(권장)

Atlas CLI로 Local Atlas Docker 이미지를 미리 받아두면 현장에서 기다림 없이 바로 시작할 수 있습니다.

→ **[Session 2 사전 준비 가이드](hands-on/session-2/prerequisites.md)**
