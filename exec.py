import weather
import line
import os 
import datetime


LINE_NOTIFY_TOKEN = os.environ["LINE_NOTIFY_TOKEN"]
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]

line_notify_client = line.LineNotify(os.environ["LINE_NOTIFY_TOKEN"])

def call():
  "call"

try:
  weather_client = weather.Weather(WEATHER_API_KEY)
  weather_data = weather_client.get_weather()
  message = "\n{}の天気({})\n----------------------------\n天気: {}\n気温: {}\n最高気温: {}\n最低気温: {}\n---------------------------- ".format(weather_data["name"],str(datetime.date.today()),weather_data["weather"][0]["description"], weather_data["main"]['temp'], weather_data["main"]['temp_max'], weather_data["main"]['temp_min'])
except Exception as e:
  print(e)
  line_notify_client.send_message("システムエラーです。")
  exit()
else: 
  status_code = line_notify_client.send_message(message)
  if status_code == 200:
    # DynamoDBに保存
     call() 