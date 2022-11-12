import requests as rt
from bs4 import BeautifulSoup as bs

url = "https://bds.oia.ntnu.edu.tw/bds/web/news-exvs/2022090502"
r = rt.get(url)
sp = bs(r.text,'html.parser')

datas = sp.find('div',class_='ckImport')
title = datas.find('big').text
print("112 semester: ",title)