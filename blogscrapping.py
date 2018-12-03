import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get('http://www.fixedgear.se/forum/')
soup = BeautifulSoup(response.text, 'html.parser')

for item in soup.select(".forumlink"):
  print(item.get_text())



print(el)