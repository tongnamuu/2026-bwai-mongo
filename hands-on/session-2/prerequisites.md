# Session 2 사전 준비 가이드

Session 2는 Session 1 준비([→ Session 1 사전 준비](../session-1/prerequisites.md))가 완료된 상태를 전제합니다. 추가로 아래 항목을 행사 전에 완료하세요.

---

## 필수: Docker 설치

MongoDB Local Atlas는 Docker 컨테이너로 실행됩니다.

```bash
docker --version
docker ps
```

설치되어 있지 않으면: https://docs.docker.com/get-docker/

Docker Desktop을 설치한 경우 앱을 실행하여 데몬이 활성화 상태인지 확인하세요. `docker ps`를 입력했을 때 에러 없이 목록이 출력되어야 합니다.

---

## 권장: Atlas CLI 설치 및 Local Atlas 초기 구동

Atlas CLI를 설치하고 Local Atlas 인스턴스를 한 번 생성해 두세요. 첫 실행 시 Docker 이미지를 다운로드하기 때문에 행사 전에 완료해 두어야 현장에서 기다림 없이 시작할 수 있습니다.

### Atlas CLI 설치

macOS (Homebrew):

```bash
brew install mongodb-atlas-cli
atlas --version
```

Windows 및 다른 설치 방법: https://www.mongodb.com/docs/atlas/cli/current/

### Local Atlas 인스턴스 초기 생성

처음 실행 시 Docker 이미지 다운로드를 포함하여 3~5분이 소요됩니다.

```bash
atlas local setup local-rag
```

실행 중 나타나는 질문:

- **setup 방식**: `With default settings` 선택
- **연결 방식**: `Skip` 선택 (`.env`를 통해 수동으로 연결 예정)

생성 후 상태와 연결 정보를 확인합니다.

```bash
atlas local list
atlas local connect local-rag --connectWith connectionString
```

> [!NOTE]
> 이미 생성한 인스턴스가 있으면 `atlas local setup`은 건너뜁니다. 현장에서는 `atlas local start local-rag`로 재기동합니다.

---

## 선택: 패키지 미리 설치

현장 네트워크 상황이 불안정할 수 있으므로, 패키지를 미리 설치해 두는 것을 권장합니다.

```bash
cd hands-on/session-2/work
uv sync
```

`uv sync`는 `pyproject.toml`을 읽어 `.venv`를 만들고 필요한 패키지를 모두 설치합니다.

---

## 트러블슈팅

**Docker가 실행되지 않음**

Docker Desktop 앱을 실행하세요. `docker ps`를 입력했을 때 에러 없이 컨테이너 목록이 출력되어야 합니다. 에러가 계속되면 Docker Desktop을 재시작하거나 재설치를 시도하세요.

**`atlas local setup` 실패**

Atlas CLI가 Docker 데몬과 통신할 수 없는 경우 발생합니다. Docker Desktop이 실행 중인지 먼저 확인하세요.

---

## 더 알아보기

- [The Voyage 4 model family](https://blog.voyageai.com/2026/01/15/voyage-4/) — 이번 실습에서 사용하는 로컬 임베딩 모델 voyage-4-nano가 속한 Voyage AI 공개 가중치 모델 패밀리 소개
- [MongoDB Atlas CLI](https://www.mongodb.com/docs/atlas/cli/current/) — CLI로 Atlas 클러스터 및 로컬 배포를 관리하는 공식 문서
- [Create a Local Atlas Deployment](https://www.mongodb.com/docs/atlas/cli/current/atlas-cli-deploy-local/) — `atlas local setup`으로 로컬 MongoDB 환경을 구성하는 방법
