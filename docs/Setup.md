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
fastapi dev main.py
```