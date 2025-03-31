from datetime import timezone

import boto3
from botocore.config import Config

class AwsS3Utils:

    @staticmethod
    def get_s3_client_with_sts(role_arn: str, role_session_name: str = "yaans-session"):
        sts_client = boto3.client("sts", region_name='ap-northeast-2')

        assumed_role = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=role_session_name,
            DurationSeconds=3600
        )

        credentials = assumed_role['Credentials']

        s3_client = boto3.client(
            "s3",
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
            config=Config(signature_version="s3v4"),
            region_name="ap-northeast-2"  # 또는 원하는 리전
        )

        return s3_client