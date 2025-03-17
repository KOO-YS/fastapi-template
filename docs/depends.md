
### Depends
- Dependency Injection 지원 기능
- 함수, 클래스의 의존성을 선언하고 지동으로 주입할 수 있도록 도움
- DB 연결, 인증, 설정 등 공통 로직을 자동으로 주입하여 코드 중복을 줄이고 유지보수를 쉽게 함

### 기본 사용법
1. 함수형 의존성 주입

선언되어 있는 **함수**
```python
from sqlalchemy.orm import Session
from app.db.database import SessionLocal

def get_db():
    """DB 세션을 생성하여 반환 (FastAPI에서 자동 주입)"""
    db = SessionLocal()
    try:
        yield db  # `yield`를 사용하여 세션을 반환
    finally:
        db.close()
```

Depends(메소드)를 이용해 의존성 주입
```python
@app.get("/items/")
async def get_items(db: Session = Depends(get_db)):
    """
    - get_db : Database 세션 생성 함수
    - `Depends(get_db)`를 사용하여 DB 세션을 자동으로 주입
    - FastAPI가 `get_db()`를 호출한 후 반환값을 `db` 매개변수에 전달
    """
    return {"message": "DB session injected successfully!"}
```
- FastAPI가 자동으로 괄호 안 함수를 실행하고 결과를 메소드에 전달


2. 클래스 기반 의존성 주입
선언되어 있는 **클래스**
```python
class Config:
    """애플리케이션 설정 관리 클래스"""
    def __init__(self):
        self.api_key = "my-secret-key"

def get_config():
    """Config 인스턴스를 생성하여 반환"""
    return Config()
```

Depends(메소드)를 이용해 의존성 주입
```python
@app.get("/config")
async def get_api_key(config: Config = Depends(get_config)):    # 객체 자체 default 값이 Depends 의존성 주입
    return {"API Key": config.api_key}

```
- 메소드의 parameter가 아닌 클래스 인스턴스를 주입할 수 있음
- 객체의 상태를 유지하면서 여러 API에 재사용 가능