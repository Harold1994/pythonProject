#encoding:utf-8
import requests
url = "https://www.amazon.cn/dp/B00OSY23CC/ref=cngwdyfloorv2_recs_0/461-0429863-0814340?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=4PCQ5S585KT7DFJD7PX3&pf_rd_t=36701&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_i=desktop&th=1"
try:
    kv = {'user-agent': "Mozilla/5.0"}#修改headers,否则user-agent不通过
    r = requests.get(url, headers=kv)
    #print r.request.headers
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print r.text[:1000]
except:
    print"爬取失败"



