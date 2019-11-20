import requests
from bs4 import BeautifulSoup

r = requests.get("https://ithelp.ithome.com.tw/articles/10192514")

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'lxml')
    
plain_text = soup.body.get_text()
plain_text = plain_text.replace(" ", "")
plain_text = plain_text.replace("\n", "")

print(plain_text)