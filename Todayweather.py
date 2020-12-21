import requests
# pip install requests
from bs4 import BeautifulSoup
# pip install beautifulsoup

search = "weather today at my location"

url = f"https://www.google.com/search?&q={search}"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

temp = soup.find("div",class_='BNeawe')                      
print(temp.text)                                 