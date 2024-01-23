import requests
from bs4 import BeautifulSoup

import tkinter as tk


def retrieve_input():
    input_value = entry.get()
    print(input_value)

    html = requests.get(
        "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
        + input_value
    )
    html = html.text

    soup = BeautifulSoup(html, "html.parser")
    links = soup.select(".news_tit")
    print(links)
    for link in links:
        title = link.text  # 링크 안에 텍스트요소 갔고옴
        url = link.attrs["href"]  # href의 속성값을 가져온다.
        print(title, url)
        return input_value


# 기본 창 설정
root = tk.Tk()
root.title("입력 받기 예제")

# Entry 위젯 설정
entry = tk.Entry(root)
entry.pack()

# 버튼 설정, 버튼을 클릭하면 retrieve_input 함수가 호출됨
button = tk.Button(root, text="입력 받기", command=retrieve_input)
button.pack()


root.mainloop()
