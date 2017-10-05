#encoding=utf-8
import os
import requests
url = 'http://image.nationalgeographic.com.cn/2017/1001/20171001034547676.jpg'
root = '/home/harold/Downloads/'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os._exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print "文件已保存"
    else:
        print "文件已存在"
except:
    print "爬取失败"


