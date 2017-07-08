from boto3.session import Session
from django.conf import settings

def retrieve_presigned_url(file_path, expires_in):
    session = Session(aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                      region_name=settings.AWS_REGION).get_session()
    return session.client('s3').generate_presigned_url('get_object',
                                                       Params={'Bucket': bucket, 'Key': file_path},
                                                       ExpiresIn=expires_in)
