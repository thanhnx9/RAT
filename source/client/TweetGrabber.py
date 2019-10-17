from bs4 import BeautifulSoup
import re
import requests
import time
from selenium import webdriver


# html = urllib.urlopen('https://twitter.com/Cryptoki').read()
# soup = soupy(html)

def tweet_scroller(url):
    path_to_chromedriver = "C:\Python27\chromedriver.exe"  # enter path of chromedriver
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    browser.get(url)
    # define initial page height for 'while' loop
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # define how many seconds to wait while dynamic page content loads
        time.sleep(3)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
    html = browser.page_source
    return html


def tweet_grab_ipC2(url):
    data = requests.get(url)
    all_tweets = list()

    html = BeautifulSoup(tweet_scroller(url), 'html.parser')
    timeline = html.select('#timeline li.stream-item')
    for tweet in timeline:
        tweet_id = tweet['data-item-id']
        tweet_text = tweet.select('p.tweet-text')[0].get_text()
        all_tweets.append({"id": tweet_id, "text": tweet_text})
    print all_tweets  # get content from page
    # x = soup.find("meta", {"name": "description"})['content']

    ip_C2 = []
    url = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    ip_C2_regex = r'[0-9]+(?:\.[0-9]+){3}'
    for i in all_tweets:
        filter = re.findall(ip_C2_regex,
                            i['text'])  # After parsing the html page, our tweet is located between double quotations
        # tweet =  filter[0]                 # using regular expression we filter out the tweet
        if len(filter) != 0:
            ip_C2.append(filter)
    return ip_C2
# url = 'https://twitter.com/ThreatHunting'
# print tweet_scrap_ipC2(url)
