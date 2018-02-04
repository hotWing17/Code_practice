#text1_下载单张图片

import requests
#引入文件操作库
import os
#为了调试方便
import traceback

url = 'http://i-4.yxdown.com/2018/2/2/KDkwMHgp/b105e361-01e6-4483-9f4a-52869a18369b.jpg'
#存储路径
root = '/home/dc/桌面/爬虫练习(一)/'
path = root + '1.jpg'

try:
    if not os.path.exists(root):
	    os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('图片下载成功')
    else:
    	print('文件已经存在')
except:
    traceback.print_exc()
    print('爬取失败')
