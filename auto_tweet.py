from typing import Text
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import weatherdef
import prac

text = prac.Weather() 
#開きたいサイト
url = "https://twitter.com/login?lang=ja"
#各種情報の入力
user_name = ''
pass_word = ''
#chromedriverの設定
driver = webdriver.Chrome(executable_path=r"C:\Users\setsuhamu\OneDrive\デスクトップ\python st\study\chromedriver.exe")
#カレントウインドウを最大化する
driver.maximize_window()
time.sleep(3)
#上で指定したサイトを開く
driver.get(url)
time.sleep(5)
#要素の指定
username = driver.find_element_by_name("session[username_or_email]")
username.send_keys(user_name)
password = driver.find_element_by_name("session[password]")
password.send_keys(pass_word)
element_login = driver.find_element_by_xpath('//*[@data-testid="LoginForm_Login_Button"]')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
element_login.click()
time.sleep(3) # 待ち

  # ツイート内容を入力
tweet = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
tweet.send_keys(text)
time.sleep(5)

#ツイートボタンをクリック
tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
tweet_button.click()
time.sleep(5)
