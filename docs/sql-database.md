# RDBMS in FastAPI
- [공식 documents](https://fastapi.tiangolo.com/ko/tutorial/sql-databases/?h=db#_11)

## SQLAlchemy
- SQL을 Python 코드로 다룰 수 있는 ORM(Object Relation Mapper)
  - 데이터 모델을 클래스로 정의하고 실제 데이터베이스 테이블과 매핑
- 2.0버전부터 FastAPI와 결합하여 async 지원
- 지원 데이터베이스
  - PostgreSQL
  - MySQL
  - SQLite
  - Oracle
  - Microsoft SQL Server ...


### SQLAlchemy 구성 요소
- `create_engine` : 데이터베이스 엔진
  - 데이터베이스 커넥션 설정 객체
  - 데이터베이스 드라이버를 통해 SQL 실행
- `SessionLocal` : 데이터베이스 세션
  - 데이터베이스와의 연결을 관리하는 세션 객체 제공

  
## Alembic
- 데이터베이스 버전관리
- 데이터베이스 스키마 변경사항을 추척 관리하여 개발 및 배포 과정에서 발생할 수 있는 문제 예방
- SQLAlchemy 개발자가 만든 데이터베이스 마이그레이션 자동화 도구
  - 마이그레이션 스크립트 생성 & 실행하여 스키마 변경
  - 마이그레이션 이력을 관리하고 롤백 기능 제공

### 데이터베이스 버전 관리의 필요성
- 스키마 변경 관리 : 애플리케이션 개발 과정에서는 데이터베이스 스키마가 빈번하게 변경됨
- 협업 효율성 향상 : 여러 개발자가 협업하는 환경에서 데이터베이스 스키마 변경 사항을 공유하고 관리하는 것이 중요. 협업 과정에서 발생할 수 있는 충돌 방지 및 효율성 증가
- 롤백 및 복구 : 잘못된 스키마 변경으로 인해 문제가 발생했을 경우, 이전 버전으로 롤백하여 데이터베이스 복구 가능
- 배포 자동화 : 버전 관리를 토해 스키마 변경 사항을 자동으로 배포환경에 적용 가능

### Alembic 사용법 
1. Alembic 설치
```shell
pip install alembic

# docker-compose를 통해 postgresql을 미리 실행
# docker compose -f docker-compose/postgresql.yml up
```

2. Alembic 환경 초기화
```shell
alembic init alembic

#  Creating directory 'fastapi-template/alembic' ...  done
#  Creating directory 'fastapi-template/alembic/versions' ...  done
#  Generating fastapi-template/alembic/script.py.mako ...  done
#  Generating fastapi-template/alembic/env.py ...  done
#  Generating fastapi-template/alembic/README ...  done
#  Generating fastapi-template/alembic.ini ...  done
#  Please edit configuration/connection/logging settings in 'fastapi-template/alembic.ini' before proceeding.
```
- alembic 폴더와 `alembic.ini` 파일 생성
```shell
alembic
├── README
├── env.py
├── script.py.mako
└── versions
```

- 1. `alembic.ini` 파일 내부 : 연동할 DB 정보 설정
  ```shell
  # 연동 DB INFO : docker-compose/postgresql.yml
  sqlalchemy.url = postgresql://postgres:1234@localhost:5432/postgres
  ```
- 2. `alembic/env.py` 파일 내부 : target_metadata 가 None으로 되어 있는 곳을 찾아 SQLAlchemy Base 모델 연결 
  ```shell
  from app.db.database import Base
  
  target_metadata = Base.metadata
  ```
  

3. 마이그레이션 생성
- alembic/versions/ 폴더에 마이그레이션 스크립트가 생성됨
```shell
alembic revision --autogenerate -m "create user tables"

#INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
#INFO  [alembic.runtime.migration] Will assume transactional DDL.
#INFO  [alembic.ddl.postgresql] Detected sequence named 'users_id_seq' as owned by integer column 'users(id)', assuming SERIAL and omitting
#INFO  [alembic.autogenerate.compare] Detected removed index 'ix_users_email' on 'users'
#INFO  [alembic.autogenerate.compare] Detected removed index 'ix_users_id' on 'users'
#INFO  [alembic.autogenerate.compare] Detected removed table 'users'
#  Generating fastapi-template/alembic/versions/ed3ccb98a6aa_create_user_tables.py ...  done
```
4. 마이그레이션 실행
```shell
# 최신 버전까지 마이그레이션을 DB에 적용
alembic upgrade head
```

- 이후 DB 설계가 변경 될 경우? -> 반복
```shell
alembic revision --autogenerate -m "..."
alembic upgrade head
```

5. 롤백