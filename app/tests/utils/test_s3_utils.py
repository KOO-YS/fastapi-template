from fastapi import HTTPException
from app.utils.s3_utils import AwsS3Utils

BUCKET_NAME = "your-bucket-name"
ROLE_ARN = "arn:aws:iam::<ACCOUNT_ID>:role/MyS3AccessRole"

# aws configure > 콘솔에서 User에 대한 Access key 생성 후 등록
# aws sts assume-role --role-arn arn:aws:iam::<ACCOUNT_ID>:role/MyS3AccessRole --role-session-name yaans-session --duration-seconds 3600

def test_get_s3():
    s3 = AwsS3Utils().get_s3_client_with_sts(ROLE_ARN)

    try:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix="/", Delimiter="/")

        directories = [content["Prefix"] for content in response.get("CommonPrefixes", [])]
        files = [content["Key"] for content in response.get("Contents", [])]

        all_items = directories + files
        return all_items

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))