from bs4 import BeautifulSoup
import requests
import sqlite3 as sq

url = ("https://www.bbc.com/ukrainian/features-66330880")

cn = sq.connect("database.sl3")
cur = cn.cursor()

cur = sq.connect("database.sl3")


cn.commit()

cn.close()

response = requests.get(url)
if response.status_code==200:
    bs = BeautifulSoup(response.text, features='html.parser')
    list = bs.find_all('h2')
    for elem in list[:10]:
        title=elem.text
        print(title)


