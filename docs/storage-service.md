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

```shell
aws configure
#AWS Access Key ID [****************ㅇㅇㅇ]: 입력
#AWS Secret Access Key [****************ㅇㅇㅇ]: 입력
#Default region name [ap-northeast-2]: ap-northeast-2
#Default output format [json]: 

aws sts assume-role --role-arn {arn-이름} --role-session-name {세션-이름} --duration-seconds 3600

#{
#    "Credentials": {
#        "AccessKeyId": "임시키",
#        "SecretAccessKey": "임시키",
#        "SessionToken": "임시토큰",
#        "Expiration": "2025-04-01T15:19:55+00:00"
#    },
#    "AssumedRoleUser": {
#        "AssumedRoleId": "임시:{세션이름}",
#        "Arn": "임시arn"
#    }
#}
```


