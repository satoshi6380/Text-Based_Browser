from requests import get

from bs4 import BeautifulSoup

i = int(input())
with get(input()) as r:
    print(BeautifulSoup(r.content, "lxml-xml").find_all('h2')[i].text)
