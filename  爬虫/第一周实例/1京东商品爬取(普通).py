#第一周实例：京东商品爬取
import requests
url = "https://item.jd.com/4099139.html"
try:
	r = requests.get(url,timeout = 30)
	r.raise_for_status()	#如果状态不是200,引发HTTPError异常
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("产生异常")
