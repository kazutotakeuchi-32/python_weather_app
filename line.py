
import requests

# Line Notify Docs
# @see https://notify-bot.line.me/doc/ja/

class LineNotify:
  def __init__(self, token):
    self.token = token

  def send_message(self, message):
    header = self.set_header()
    data = self.set_data(message)
    url = "https://notify-api.line.me/api/notify"
    r = requests.post(url, headers=header, data=data)
    return r.status_code

  def set_header(self):
    header = {}
    header["Authorization"] = "Bearer " + self.token
    header["Content-Type"] = "application/x-www-form-urlencoded"
    return header
  
  def set_data(self, message):
    data = {}
    data["message"] = message
    return data

  #   message += "****東京の天気*****\n"
  #   message += "---------------------------\n"
  #   message += "日付: " + row['dt_txt'] + "\n"
  #   message += "天気: " + row['weather'][0]['description']+ "\n"
  #   message += "気温: " + str(row['main']['temp']) + "℃\n"
  #   message += "---------------------------\n"
