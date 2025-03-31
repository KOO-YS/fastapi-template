# Binding Storage Service

## AWS S3 안전하게 연동하는 법 : Assume Role

- 기존의 aws 연동 작업의 경우 Access key를 서버나 코드에 직접 등록하는 방식을 사용하며 보안적으로 위험성을 가지고 있다

### Assume Role
- 특정 권한을 일시적으로 빌려서 사용할 수 있음
- 사용자에게 직접 접근 권한을 주지 않고 **리소스 접근 정책과 관련있는 임시 토큰을 발급**받아 사용
  - STS : Security Token Service. 외부에서 role을 assume해서 임시 자격을 얻을 수 있음

- aws 상에서 role 권한 추가
```shell
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "*"
        }
    ]
}
```