#coding:utf-8
import requests


def getHTMLText(url):
    try:
        r = requests.head(url)
        #r.raise_for_status()
        #r.encoding = r.apparent_encoding
        return r
    except:
        return "产生异常"


if __name__=="__main__":
    url = "http://www.baidu.com"
    print getHTMLText(url)
