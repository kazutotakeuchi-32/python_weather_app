import boto3

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