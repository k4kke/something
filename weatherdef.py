#ライブラリのインポート
import requests
from bs4 import BeautifulSoup

def tenki():
  #tenki.jp神戸地域のページのURL
  url = 'https://tenki.jp/forecast/6/31/6310/28110/'

  #HTTPリクエスト
  r = requests.get(url)



  #HTMLの解析
  bsObj = BeautifulSoup(r.content, "html.parser")

  #今日の天気を取得
  today = bsObj.find(class_="today-weather")
  weather = today.p.string

  #気温情報のまとまり
  temp=today.div.find(class_="date-value-wrap")

  #気温の取得
  temp=temp.find_all("dd")
  temp_max = temp[0].span.string #最高気温
  temp_max_diff=temp[1].string #最高気温の前日比
  temp_min = temp[2].span.string #最低気温
  temp_min_diff=temp[3].string #最低気温の前日比

  main_text = '===神戸市の今日の天気===' + '\n' +"天気:{}".format(weather) + '\n' + "最高気温:{}".format(temp_max) + '\n' +"最低気温:{}".format(temp_min) 

  return main_text

