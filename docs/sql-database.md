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

  
