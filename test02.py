# test02 : requests + BeautifulSoup으로 네이버 뉴스 크롤링
import requests
from bs4 import BeautifulSoup

HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"}

# 대상 url
url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&listType=summary&sid1=001&date=20231001&page=1'

req = requests.get(url, headers=HEADER) # requests.get : HTTP 프로토콜을 사용하여 웹 서버에게 정보를 요청

html = req.text

soup = BeautifulSoup(html, 'html.parser')

# type06_headline : 상위 10개
news_headline_container = soup.select_one('ul.type06_headline')

news_headline_list = news_headline_container.select('dt:not(.photo) > a')

news_titles = []
for news in news_headline_list : news_titles.append(news.text.strip())

# type06 : 하위 10개
news_container = soup.select_one('ul.type06')

news_list = news_container.select('dt:not(.photo) > a')

for news in news_list : news_titles.append(news.text.strip())

for titles in news_titles : print(titles) # 최근 기사 제목 20개 가져옴