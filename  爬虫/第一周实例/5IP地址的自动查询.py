#IP地址的自动查询
import requests
url = "http://m.ip138.com/ip.asp?ip="	#上网站随便搜索一个地址，查询‘查询IP地址的url格式’
try:
	r = requests.get(url + '202.204.80.112')
	r.raise_for_status()	#如果状态不是200,引发HTTPError异常
	r.encoding = r.apparent_encoding
	print(r.text[-500:])	#输出后500个字符
except:
	print("产生异常")
