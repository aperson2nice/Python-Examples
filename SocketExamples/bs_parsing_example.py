import requests
from bs4 import BeautifulSoup

URL = 'http://econpy.pythonanywhere.com/ex/001.html'

req = requests.get(URL)

soup = BeautifulSoup(req.text, 'html.parser')

for buyer_info in soup.find_all('div', {'title': 'buyer-info'}):
    print(buyer_info.text.lstrip())
    