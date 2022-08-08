import datetime
import dydb
import csv
import s3
import os

class HelperFunction:
  @staticmethod
  def set_pre_1_weeks():
    today_date = datetime.date.today()
    i = 0
    keys = []
    while i < 7:
      keys.append(str(today_date - datetime.timedelta(days=i)) + "Tokyo")
      i+=1
    return keys

  @staticmethod
  def get_weather():
    pre_1_weeks_weather = []
    keys = HelperFunction.set_pre_1_weeks()
    db = dydb.Db('dynamodb', os.environ['TABLE_NAME'])
    for key in keys:
      pre_1_weeks_weather.append(db.select(key))
    return pre_1_weeks_weather

  @staticmethod 
  def execute():
    try:
      # 天気情報をDynmoDBを取得
      weather_data = HelperFunction.get_weather()
      csv_file = HelperFunction.write_csv(weather_data)
      #S3に保存
      s3.S3Base(os.environ["BUCKET_NAME"]).upload("/tmp/tmp.csv", "/tmp/tmp.csv")
    except Exception as e:
      raise e
    else:
      HelperFunction.remove_csv()
  @staticmethod
  def write_csv(data):
    with open('/tmp/tmp.csv', 'w') as f:
      writer = csv.DictWriter(f, data[0].keys())
      writer.writeheader()
      for row in data :
        writer.writerow(row)
  
  @staticmethod
  def remove_csv():
    os.remove("/tmp/tmp.csv")
  
