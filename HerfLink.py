#encodiong=utf-8
import requests
import re
from bs4 import BeautifulSoup
r = requests.get("https://www.python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
for link in soup(string = re.compile("python")):
    print link
