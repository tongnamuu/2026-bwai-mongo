# Session 2 로컬 RAG 사전 준비 가이드

[메인 안내로 돌아가기](../README.md)

Session 2는 Session 1 준비가 끝난 상태를 전제로 합니다. 추가로 MongoDB Local Atlas, Python 패키지, 로컬 임베딩 모델, Jupyter 노트북 실행 환경을 행사 전에 준비해 주세요.

## 준비 요약

현장 실습에서 기다리지 않으려면 아래 항목을 미리 끝내는 것을 권장합니다.

1. Docker Desktop 설치 및 실행 확인
2. Atlas CLI 설치
3. Local Atlas 인스턴스 1회 생성으로 Docker 이미지 다운로드 완료
4. Session 2 Python 패키지 설치 완료 (`uv sync`)
5. `voyageai/voyage-4-nano` 임베딩 모델 사전 다운로드 완료
6. Jupyter 노트북을 실행할 수 있는 편집기와 Jupyter 확장 프로그램 준비

MongoDB 문서 실습 데이터(`hands-on/session-2/data/mongodb_docs.json`)는 저장소에 포함되어 있으므로 별도로 다운로드하지 않아도 됩니다. 외부 API 키도 필요하지 않습니다.

## 1. Session 1 기반 환경 확인

Session 2에서도 Ollama Gemma 4, Python, `uv`를 사용합니다.

```bash
python --version
uv --version
ollama list
```

`ollama list`에 행사에서 사용할 Gemma 4 모델 태그가 보여야 합니다. 기본값은 `gemma4:e4b`입니다.

```bash
ollama pull gemma4:e4b
```

Gemma 4 모델은 수 GB이므로 행사장에서 새로 다운로드하지 않는 것을 권장합니다. 8GB 메모리 장비는 `gemma4:e2b`를 대체 모델로 준비하세요.

## 2. Docker 설치

MongoDB Local Atlas는 Docker 컨테이너로 실행됩니다.

```bash
docker --version
docker ps
```

설치되어 있지 않으면 Docker 공식 설치 문서를 확인하세요.

```text
https://docs.docker.com/get-docker/
```

Docker Desktop을 설치한 경우 앱을 실행하여 데몬이 활성화 상태인지 확인하세요. `docker ps`를 입력했을 때 에러 없이 목록이 출력되어야 합니다.

## 3. Atlas CLI 설치 및 Local Atlas 초기 구동

Atlas CLI를 설치하고 Local Atlas 인스턴스를 한 번 생성해 두세요. 첫 실행 시 Docker 이미지를 다운로드하기 때문에 행사 전에 완료해 두어야 현장에서 기다림 없이 시작할 수 있습니다.

macOS Homebrew:

```bash
brew install mongodb-atlas-cli
atlas --version
```

Windows 및 다른 설치 방법은 MongoDB Atlas CLI 공식 문서를 따릅니다.

```text
https://www.mongodb.com/docs/atlas/cli/current/
```

처음 실행 시 Docker 이미지 다운로드를 포함하여 3~5분 정도 걸릴 수 있습니다.

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

이미 생성한 인스턴스가 있으면 `atlas local setup`은 건너뜁니다. 현장에서는 `atlas local start local-rag`로 재기동합니다.

## 4. Python 패키지 미리 설치

현장 네트워크 상황이 불안정할 수 있으므로, Session 2 패키지를 미리 설치해 두는 것을 권장합니다.

```bash
cd hands-on/session-2/work
uv sync
```

`uv sync`는 `pyproject.toml`을 읽어 `.venv`를 만들고 필요한 패키지를 모두 설치합니다.

## 5. 임베딩 모델 미리 다운로드

Session 2에서 문서와 질문을 벡터로 바꾸려면 로컬 임베딩 모델인 `voyageai/voyage-4-nano`가 필요합니다. 노트북의 임베딩 단계에서 `sentence-transformers`가 HuggingFace에서 자동으로 다운로드하지만, 최초 1회 다운로드가 필요하므로 행사 전에 미리 받아두세요.

먼저 Session 2 패키지를 설치합니다.

```bash
cd hands-on/session-2/work
uv sync
```

그다음 임베딩 모델을 로컬 HuggingFace 캐시에 다운로드합니다.

```bash
cd hands-on/session-2/work
uv run python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('voyageai/voyage-4-nano', trust_remote_code=True); print('voyage-4-nano cached')"
```

처음 실행 시 모델 파일 다운로드로 1~2분 정도 걸릴 수 있습니다. `voyage-4-nano cached`가 출력되면 사전 다운로드가 끝난 상태입니다. 이후에는 로컬 HuggingFace 캐시에서 불러옵니다.

## 6. 노트북 편집 환경 준비

Session 2 실습은 `hands-on/session-2/work/rag_pipeline.ipynb`에서 진행합니다. Antigravity IDE 또는 VS Code처럼 Jupyter 노트북을 열고 실행할 수 있는 편집기를 준비하세요.

필수/권장 확장 프로그램:

- **Jupyter** (`ms-toolsai.jupyter`) [필수]: 노트북 실행과 커널 선택에 필요합니다.
- **MongoDB for VS Code** (`mongodb.mongodb-vscode`) [추천]: Local Atlas에 적재된 컬렉션과 문서를 편집기 안에서 확인할 수 있습니다.
- **Markdown Preview Mermaid Support** (`bierner.markdown-mermaid`) [선택]: README의 Mermaid 아키텍처 다이어그램을 그래픽으로 확인할 때 사용합니다.

`uv sync`를 완료한 뒤 노트북에서 커널을 선택할 때 `hands-on/session-2/work/.venv` 환경을 선택하세요. 자동으로 보이지 않으면 편집기를 한 번 재시작하거나 `Python: Select Interpreter`에서 `.venv`의 Python 경로를 직접 지정합니다.

## 자주 생기는 문제

### Docker가 실행되지 않습니다

Docker Desktop 앱을 실행하세요. `docker ps`를 입력했을 때 에러 없이 컨테이너 목록이 출력되어야 합니다. 에러가 계속되면 Docker Desktop을 재시작하거나 재설치를 시도하세요.

### `atlas local setup`이 실패합니다

Atlas CLI가 Docker 데몬과 통신할 수 없는 경우 발생합니다. Docker Desktop이 실행 중인지 먼저 확인하세요.

### `voyageai/voyage-4-nano` 다운로드가 실패합니다

네트워크 연결 또는 HuggingFace 접속 정책을 확인하세요. 회사/학교 네트워크에서 HuggingFace 다운로드가 차단될 수 있으므로, 가능하면 행사 전에 다른 네트워크에서 위 모델 캐시 명령을 한 번 실행해 두세요.
