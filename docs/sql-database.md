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
2. Alembic 환경 초기화
3. 마이그레이션 스크립트 생성
4. 마이그레이션 실행
5. 롤백