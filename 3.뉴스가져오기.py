import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%95%A0%ED%94%8C"
)
html = html.text

soup = BeautifulSoup(html, "html.parser")
links = soup.select(".news_tit")
print(links)
for link in links:
    title = link.text  # 링크 안에 텍스트요소 갔고옴
    url = link.attrs["href"]  # href의 속성값을 가져온다.
    print(title, url)
