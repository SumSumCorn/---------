import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com")
html = response.text
soup = BeautifulSoup(html, "html.parser")
word = soup.select("#header .imgsvg ico_naver")
# word = soup.select(".service_name")
print(word)
