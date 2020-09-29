from requests import get

from bs4 import BeautifulSoup

i = int(input())
with get(input()) as r:
    print(BeautifulSoup(r.content, "lxml-html").find_all('a')[i - 1].attrs['href'])
