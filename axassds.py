import sqlite3

from bs4 import BeautifulSoup
import requests
import sqlite3 as sq

url = ("https://www.bbc.com/ukrainian/features-66330880")

response = requests.get(url)
if response.status_code==200:
    bs = BeautifulSoup(response.text, features='html.parser')
    list = bs.find_all('h2')
    for elem in list[:10]:
        title=elem.text
        print(title)

        connect = sqlite3.connect("databasefinal.sl3")