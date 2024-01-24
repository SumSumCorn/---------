import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("hello")
keyword = st.text_input("검색어 입력")

if keyword:
    html = requests.get(
        "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
        + keyword
    )
    html = html.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".news_tit")
    st.write(links)
    for link in links:
        title = link.text  # 링크 안에 텍스트요소 갔고옴
        url = link.attrs["href"]  # href의 속성값을 가져온다.
        st.write(title, url)
