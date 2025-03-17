# Setup : Get Started


### set Python 3.12 version Using pyenv

```shell
# 3.12 버전 설치
pyenv install 3.12

# 설치된 버전 정보 조회
pyenv versions

# 현 path에서 사용할 python version 선택
pyenv local 3.12

# 적용을 위한 zsh 재실행 
exec zsh

python -V
```

### set virtual environment
```shell
python -m venv venv
```

### FastAPI Required Package

```shell
pip install "fastapi[standard]"
```

in `requirements.txt`
```shell
fastapi # framework 설치
uvicorn # ASGI(Asynchronous Server Gateway Interface) 서버로 FastAPI 실행
```

```
fastapi dev app/main.py
```

<hr>


## FastAPI 

FastAPI는 Python 기반의 비동기(Async) 웹 프레임워크

RESTful API 및 비동기 API 개발을 빠르고 효율적으로 수행할 수 있도록 설계

Python 3.7 이상에서 지원되며, Pydantic과 Starlette 기반으로 동작

🚀 FastAPI는 Flask보다 빠르고, Django보다 가벼우며, 자동 문서화 기능까지 지원하는 강력한 웹 프레임워크

<hr>

1️⃣ 성능이 뛰어남 (비동기 지원)

- 비동기(Async) 지원: async/await을 활용하여 비동기 처리를 최적화
- Starlette 기반으로 설계되어 Flask보다 훨씬 빠름
- Node.js 및 Go와 유사한 수준의 성능 제공

> 🚀 FastAPI는 성능 면에서 Uvicorn과 함께 사용하면, Flask보다 최대 2배 이상 빠른 속도를 제공할 수 있음.

2️⃣ 자동 문서화 (Swagger / ReDoc)

- API를 정의하면 자동으로 문서(Swagger UI 및 ReDoc)를 생성하여 제공
- API 문서는 default 확인 경로 
  - http://localhost:8000/docs(Swagger)
  - http://localhost:8000/redoc(ReDoc)

3️⃣ 데이터 검증 및 직렬화 (Pydantic 사용)

- Pydantic을 사용하여 데이터 검증 및 JSON 직렬화(Serialization)를 지원
- 요청(Request)과 응답(Response)의 데이터 검증을 자동으로 수행

- 📌 데이터 검증 예제
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
name: str
price: float
is_offer: bool = False

@app.post("/items/")
async def create_item(item: Item):
return {"item_name": item.name, "price": item.price}
```

✔ 위 코드에서는 Item 모델을 정의하고, 요청 데이터의 유효성을 자동으로 검증함 ✅


4️⃣ 강력한 타입 기반 코드 자동완성 (Type Hints 지원)

- FastAPI는 Python의 타입 힌트(Type Hinting)를 활용하여 코드 자동완성을 지원
IDE(PyCharm, VSCode 등)에서 빠른 개발이 가능하도록 도움
- 📌 타입 힌트 예제
```python
@app.get("/add")
async def add_numbers(a: int, b: int) -> int:
return a + b
```
✔ a: int, b: int를 선언하면 자동으로 요청 데이터 검증이 수행됨 ✅

<hr>


## Uvicorn

- ASGI(Asynchronous Server Gateway Interface) 기반의 고성능 Python 웹 서버
- FastAPI, Django, Starlette 등 비동기(Async) 웹 프레임워크와 함께 사용
- 비동기 이벤트 루프와 멀티스레딩을 활용하여 빠른 응답 속도를 제공

- 🚀 Uvicorn은 Flask/Django의 WSGI 서버(Gunicorn)보다 빠르고, 비동기 I/O를 완벽 지원하는 경량 ASGI 서버

### Uvicorn의 주요 특징
- ASGI(비동기 지원) 서버 → async/await 기반으로 비동기 API 성능 최적화
- Gunicorn보다 가볍고 빠름 → 낮은 메모리 사용량, 빠른 부팅 속도
- 멀티프로세싱 및 멀티스레딩 지원 → `--workers` 옵션으로 확장 가능
- Hot Reload 지원 → --reload 옵션으로 코드 변경 시 자동 재시작
- WebSocket 및 HTTP/2 지원 → 최신 프로토콜 지원
- Gunicorn과 함께 사용 가능 → `gunicorn -k uvicorn.workers.UvicornWorker` 조합 가능

<hr>

### `fastapi` 명령어 대신 `uvicorn` 명령어로 서버 실행

```shell
uvicorn [./패키지경로.경로2.]main:app --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Uvicorn 단독 실행은 싱글 프로세스로 동작하지만, Gunicorn과 함께 실행하면 멀티프로세싱 성능이 향상
```shell
pip install gunicorn

# Gunicorn + Uvicorn 실행 (4개 프로세스 -> CPU 코어수에 맞게 조정)
gunicorn -k uvicorn.workers.UvicornWorker -w 4 app.main:app
```