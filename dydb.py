import boto3

# DynamoDB

class Db:
  def __init__(self,resource,table_name):
    dynamoDB = boto3.resource(resource)
    self.table= dynamoDB.Table(table_name)

  def insert(self, data):
    try:
      self.table.put_item(Item = data)
    except Exception as e:
      raise e
    else:
      return True
  
  def select(self, id):
    try:
      print(id)
      response = self.table.get_item( Key={
            'id': id
      })

    except Exception as e:
      pass
    else:
      if "Item" in response.keys() :
        return response["Item"]
      else:
        return { 'condition': "", 'temp_highest': 0, 'temp': 0, 'id': id,'temp_lowest': 0}
       
  