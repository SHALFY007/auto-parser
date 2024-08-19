from bs4 import BeautifulSoup
import requests

url = ''
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

print(soup)