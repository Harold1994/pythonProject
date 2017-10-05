#encoding=utf-8
#百度关键词:www.baidu.com/s?wd=keyword
import requests
kv = {"wd":"python"}
try:
    r = requests.get('http://www.baidu.com/s',params=kv)
    print r.request.url
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print len(r.text)
except:
    print "爬取失败"