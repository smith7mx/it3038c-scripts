from bs4 import BeautifulSoup
import requests, re

r = requests.get('whitehouse.gov').content
soup = BeautifulSoup(r, "lxml")
for link in soup.find_all('a', attrs={'href':re.compile("^http")}): 
    print(link.get('href'))