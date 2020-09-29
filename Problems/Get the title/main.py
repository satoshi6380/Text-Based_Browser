import requests

import bs4

url = input()
res = requests.get(url)
print(bs4.BeautifulSoup(res.content, 'html').find('h1').text if res else '')
