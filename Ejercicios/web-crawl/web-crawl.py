from bs4 import BeautifulSoup
import requests

SITE = "http://fuente.kodivertidoteam.es/"
r  = requests.get(SITE)
data = r.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(SITE +link.get('href'))

