import boto3

class S3Base:
  def __init__(self, aws_access_key_id, aws_secret_access_key
    self.s3 = boto3.client(
      's3',
      aws_access_key_id= aws_access_key_id,
      aws_secret_access_key= aws_secret_access_key,
      region_name='ap-northeast-1'
    )

  def upload(self, file_name, file_path):
    self.s3.upload_file(file_path, self.bucket_name, file_name)

  def download(self, file_name, file_path):
    self.s3.download_file(self.bucket_name, file_name, file_path)
