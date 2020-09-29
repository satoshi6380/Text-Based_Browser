import sys
import os
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore

args = sys.argv
os.makedirs(args[1], exist_ok=True)

his = []
colorama.init(autoreset=True)

while True:

    url = input()
    if url == 'back':
        if len(his) > 1:
            del his[-1]
            with open(his[-1]) as f:
                for line in f.readlines():
                    print(line, end='')
        else:
            pass
    elif url == 'exit':
        exit()
    else:
        try:
            url = url if url.startswith('https://') or url.startswith('http://') else 'https://' + url
            var = url.replace('https://', '').replace('.', '_')
            r = requests.get(url)
            if r:
                soup = BeautifulSoup(r.content, 'html.parser')
                with open(args[1] + '/' + var, mode='w') as f:
                    for t in soup.find_all({'a', 'p', 'li', 'ul', 'ol'}):
                        print(t.text, file=f, flush=True)
                        print(Fore.BLUE + t.text if t.name == 'a' else t.text)
                    his.append(f.name)
        except Exception as e:
            print('Error: Incorrect URL')


