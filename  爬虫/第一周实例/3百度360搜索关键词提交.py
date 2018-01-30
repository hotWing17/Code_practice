#百度360搜索关键词提交
#百度的关键词接口：
#http://www.baidu.com/s?wd=keyword

import requests
try:
	kv = {'wd':'Python'}
	r = requests.get("http://www.baidu.com/s",params=kv)	#将wd字段后面换成Python
	print(r.request.url)	#查看提交给网页的url是什么
	print(len(r.text))
	r.raise_for_status()	#如果状态不是200,引发HTTPError异常
	r.encoding = r.apparent_encoding
except:
	print("产生异常")
