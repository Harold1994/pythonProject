#encoding=utf-8
import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
# print soup.title

# tag = soup.a#只返回一个
# print tag
# print soup.a.parent.parent.name
print (soup.p)
print (soup.p.string)