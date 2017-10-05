#encoding=utf-8
import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

#----------------------
#下行遍历
# print soup.head
# print soup.head.contents
# print soup.body.contents[1]
# print len(soup.body.contents)
#----------------------
#上行遍历
# print soup.title.parent
# print soup.title.parents
# print soup.html.parent
#----------------------
#平行遍历
print soup.a.previous_sibling
print soup.a.next_sibling.next_sibling
for sibling in soup.a.next_siblings:
    print sibling