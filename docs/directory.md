# Directory : FastAPI architecture

## `__init__.py` 파일

`__init__.py` 파일은 Python이 해당 디렉토리를 패키지로 인식하도록 하는 역할

- `__init__.py`가 없으면 해당 디렉토리는 일반 폴더로 인식되며, import 불가능
- `__init__.py`가 있으면 Python 패키지로 인식되며, 내부 모듈을 import 가능


- 🚀 fast_package 디렉토리를 패키지로 인식
```shell
fastapi_project/
┣ fast_package/  <-- Python이 패키지로 인식
┃ ┣ __init__.py
┃ ┣ module1.py
┃ ┗ module2.py
┗ main.py
```
✔ fast_package/ 내부에 __init__.py가 있어야 import fast_package.module1 가능

### `__init__.py` 활용
- `__init__.py`에서 미리 내부 모듈을 import 하여 타 패키지에서 모듈 이름을 생략한 채로 한 줄에 import 가능
- `__init__.py` 내부에 패키지 설정 및 초기화 코드 실행


## Directories 구성

tree 형식으로 보는 directory 구조
```shell
📂 fastapi_project
 ┣ 📂 app                # 메인 애플리케이션
 ┃ ┣ 📂 api              # API 라우트 (엔드포인트)
 ┃ ┃ ┣ 📂 v1             # API 버전 1
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┣ 📜 user_routes.py
 ┃ ┣ 📂 core             # 설정, 보안, 미들웨어
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 config.py      # 환경 변수 설정
 ┃ ┃ ┣ 📜 security.py    # JWT 인증 관련 로직
 ┃ ┃ ┣ 📜 middleware.py  # 커스텀 미들웨어
 ┃ ┃ ┗ 📜 exception_handler.py # 글로벌 예외 처리
 ┃ ┣ 📂 db               # 데이터베이스 관련 모듈
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 database.py    # DB 연결 관리
 ┃ ┃ ┣ 📜 models.py      # SQLAlchemy 모델 정의
 ┃ ┃ ┗ 📜 crud.py        # CRUD 로직
 ┃ ┣ 📂 services         # 서비스 레이어 (비즈니스 로직)
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 user_service.py
 ┃ ┃ ┣ 📜 auth_service.py
 ┃ ┃ ┗ 📜 item_service.py
 ┃ ┣ 📂 utils            # 공통 유틸리티 함수
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 logger.py      # 로깅 설정
 ┃ ┃ ┗ 📜 helpers.py     # 유틸리티 함수 모음
 ┃ ┣ 📂 tests            # 테스트 코드
 ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┣ 📜 test_users.py
 ┃ ┣ 📜 main.py          # FastAPI 애플리케이션 시작점
 ┃ ┗ 📜 __init__.py
 ┣ 📜 .env               # 환경 변수 파일
 ┣ 📜 requirements.txt   # 패키지 목록
 ┣ 📜 docker-compose.yml # Docker 환경 설정
 ┣ 📜 Dockerfile         # Docker 빌드 파일
 ┗ 📜 README.md          # 프로젝트 문서
```
