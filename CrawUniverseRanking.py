#encoding=utf-8
import bs4
import requests
import sys
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUniList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        #过滤非标签类
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUNiList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:{3}^10}"
    print (tplt.format("排名","学校名称","地址",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print (tplt.format(u[0],u[1],u[2],chr(12288))) 

def main():

    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html  = getHTMLText(url)
    fillUniList(uinfo,html)
    printUNiList(uinfo,20)#print 20 university

main()