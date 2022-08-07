import boto3

# DynamoDB

class Db:
  def __init__(self,resource,table_name):
    dynamoDB = boto3.resource(resource)
    self.table= dynamoDB.Table(table_name)

  def insert(self, data):
    try:
      self.table.put_item(Item = data)
    except Exception, e:
      raise e
    else:
      return True
  
  def select(self, key):
    try:
      response = self.table.get_item(Key = key)
    except Exception, e:
      raise e
    else:
      return response["Item"]

  