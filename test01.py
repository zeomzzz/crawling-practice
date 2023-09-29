import requests
from bs4 import BeautifulSoup

keyword = "뱃지"

# 대상 url
url = f'https://search.shopping.naver.com/search/all?query={keyword}'

req = requests.get(url) # requests.get : HTTP 프로토콜을 사용하여 웹 서버에게 정보를 요청

html = req.text

soup = BeautifulSoup(html, 'html.parser')

result_list = soup.select_one('div.basicList_list_basis__uNBZx') # 상품 목록 리스트 영역

product_list = result_list.select('div.product_item__MDtDF > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_title__Mmw2K > a')

product_names = []
for product in product_list :
    name = product['title']
    product_names.append(name)

print(product_names) # ['다양한 뱃지 주문제작 금속배지 컬러뺏지 대량 소량 주문가능', '[5+1]캐릭터 금속 어몽어스 뱃지 벳지 배지 배찌 소량제작 브로치'] : 두 개 밖에 못 가져옴.. 왜?