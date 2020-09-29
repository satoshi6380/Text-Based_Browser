from requests import get

from bs4 import BeautifulSoup

word = input()
with get(input()) as r:
    for p in BeautifulSoup(r.content, "lxml-html").find_all('p'):
        if word in p.text:
            print(p.text)
            break
