import tweepy
import os
import time
from selenium import webdriver
chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

CONSUMER_KEY = os.environ.get("LOGISTIBOT_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("LOGISTIBOT_CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("LOGISTIBOT_ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("LOGISTIBOT_ACCESS_SECRET")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    driver.get("https://harryparkdotio.github.io/logistify/")
    p_element = driver.find_element_by_id(id_='much-logistic')
    api.update_status(p_element.text)
    print(p_element.text)
    time.sleep(10)
