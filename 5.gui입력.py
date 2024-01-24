import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext


def fetch_and_parse(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.get_text()
    except Exception as e:
        return str(e)


def on_submit():
    url = url_entry.get()
    parsed_text = fetch_and_parse(url)
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.INSERT, parsed_text)
    result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Web Scraper with Tkinter")

tk.Label(root, text="Enter URL:").pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()
tk.Button(root, text="Fetch and Parse", command=on_submit).pack()

result_text = scrolledtext.ScrolledText(root, width=70, height=20)
result_text.pack()
result_text.config(state=tk.DISABLED)

root.mainloop()
