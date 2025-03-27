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

## Alembic 사용법 
### 1. Alembic 설치
```shell
pip install alembic

# docker-compose를 통해 postgresql을 미리 실행
# docker compose -f docker-compose/postgresql.yml up
```

### 2. Alembic 환경 초기화
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
  

### 3. 마이그레이션 생성
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


### 4. 마이그레이션 실행
```shell
# 최신 버전까지 마이그레이션을 DB에 적용
alembic upgrade head
```

- **이후 DB 설계가 변경 될 경우?** -> **반복**
```shell
alembic revision --autogenerate -m "..."
alembic upgrade head
```

### 5. 롤백
```shell
# -1 : 한단계 전 버전으로 롤백
alembic downgrade -1

# <revision_id> : 특정 revision 버전으로 롤백
alembic downgrade <revision_id>
```

### 6. 히스토리 확인
```shell
[21:03:38] [~/Documents/workspace-git/fastapi-template] [main ✖] ❱❱❱ alembic history --verbose
#Rev: ed3ccb98a6aa (head)
#Parent: <base>
#Path: fastapi-template/alembic/versions/ed3ccb98a6aa_create_user_tables.py
#
#    create user tables
#    
#    Revision ID: ed3ccb98a6aa
#    Revises: 
#    Create Date: 2025-03-26 20:11:24.369548
```

### 7. 마이그레이션 정보 Export / Import

**DDL**
```shell
# 전체 DDL 내보내기 (현재 모델 기준)
# pip install sqlacodegen
sqlacodegen postgresql://postgres:1234@localhost:5432/postgres --outfile schema.sql


alembic upgrade head --sql > upgrade.sql
alembic downgrade -1 --sql > downgrade.sql
```

> DDL export 결과
```shell
from sqlalchemy import Index, Integer, PrimaryKeyConstraint, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
        Index('ix_users_email', 'email', unique=True),
        Index('ix_users_id', 'id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)

```

**DML**
- alembic 은 스키마(DDL) 전용 도구이기 때문에 데이터 백업은 따로 진행할 필요
- pg_dump : 데이터베이스 백업 수행 명령어
  - postgresql 이 설치될 때 함께 설치된다
```shell
# DML 내보내기 in container
docker exec -it <container_id> pg_dump -U postgres --column-inserts --data-only postgres > backup.sql

# 같은 방법으로 DDL 스키마만 백업하는 방법
docker exec -it <container_id> pg_dump -U postgres -s postgres > backup-schema.sql
```
> DDL export 결과
```shell
--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4 (Debian 17.4-1.pgdg120+2)
-- Dumped by pg_dump version 17.4 (Debian 17.4-1.pgdg120+2)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.alembic_version (version_num) VALUES ('ed3ccb98a6aa');


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.users (id, name, email) VALUES (1, 'test', 'ee');


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- PostgreSQL database dump complete
--


```

---

### `alembic_version` 테이블
- alembic이 내부적으로 이 테이블을 사용하여 마이그레이션 상태 추적
- 현재 적용된 revision ID가 저장되어 있음
- UI에서 이 테이블을 직접 조회하면 현재 DB의 마이그레이션 상태를 알 수 있다
