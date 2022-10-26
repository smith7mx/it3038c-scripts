from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://uc.edu/about/factsheet.html')
soup=BeautifulSoup('\n'.join(r.text.splitlines()), 'lxml')
for x in soup.find_all('ul'):
    if('Undergraduate' in x.text):
        print(x)
        break
        