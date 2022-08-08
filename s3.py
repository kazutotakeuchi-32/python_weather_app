import boto3

class S3Base:
  def __init__(self, bucket_name):
    self.s3 =  boto3.client('s3')
    self.bucket_name = bucket_name

  def upload(self, file_name, file_path):
    self.s3.upload_file(file_path, self.bucket_name, file_name)

  def download(self, file_name, file_path):
    self.s3.download_file(self.bucket_name, file_name, file_path)

