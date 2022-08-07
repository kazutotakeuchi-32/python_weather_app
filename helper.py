import datetime
import dydb
import csv
class HelperFunction:
  @staticmethod
  def set_pre_1_weeks():
    today_date = datetime.date.today()
    i = 0
    keys = []
    while i < 7:
      keys.append(str(today_date - datetime.timedelta(days=i)) + "tokyo")
      i+=1
    return keys

  @staticmethod
  def get_weather():
    pre_1_weeks_weather = []
    keys = HelperFunction.set_pre_1_weeks()
    db = dydb.Db('dynamodb','weather')
    for key in keys:
      pre_1_weeks_weather.append(db.select(key))
    csv.write(pre_1_weeks_weather)
  
keys= HelperFunction.set_pre_1_weeks()
print(keys)
