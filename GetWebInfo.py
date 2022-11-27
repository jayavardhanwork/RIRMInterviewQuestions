
from bs4 import BeautifulSoup
import requests

url = 'https://ful.io'
req = requests.get(url)

soup = BeautifulSoup(req.text, "html.parser")
  
child_soup = soup.find_all('a')
  
for link in soup.find_all('a'):
    if(link.get('href').string == 'tel'):
        print(link.get('href'))
