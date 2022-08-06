import requests # pip install requests

class Weather:

  def __init__(self, key):
    self.api_key = key

  def get_weather(self):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
      "q": "tokyo",
     "appid": self.api_key, 
      "units": "Metric",
      "lansg": "ja"
    }
    r = requests.get(url, params=params)
    return r.json()


