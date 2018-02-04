#网络图片爬取与存储

import requests
import os									#引入文件操作库
url = "http://image.nationalgeographic.com.cn/2018/0112/20180112011553162.jpg"
root = "/home/dc/桌面/爬虫/第一周实例/图片/"			#存储路径
path = root + url.split('/')[-1]					#截取原名字（url最后字符串）作为爬取后的图片名字
try:
	if not os.path.exists(root):			#判断当前根目录是否存在
		os.mkdir(root)						#不存则创建目录
	if not os.path.exists(path):			#判断文件是否存在，不存在就要执行操作
		r = requests.get(url)
		with open(path,'wb') as f:			#对二进制文件操作时使用‘wb’,
			f.write(r.content)				#图片是二进制形式的文件
			f.close()
			print("文件保存成功")
	else:									#该文件已经存在
		print("文件已存在")
except:
	print("爬取失败")
	

#文件操作的with语句作用	
#1、自动管理文件对象，不需要调用close()
#2、强的鲁棒性；当遭遇程序bug时导致本来应有的close()未能执行，如果使用with，python保证即使出现故障，也能保证文件被正确关闭
