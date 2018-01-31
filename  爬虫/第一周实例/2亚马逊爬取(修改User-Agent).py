#r.request.headers		查询发给url的头信息

#亚马逊爬取(修改User-Agent)
import requests
url = "https://www.amazon.cn/gp/product/B06XXRNFZ9?pf_rd_m=A1AJ19PSB66TGU&storeType=ebooks&pageType=STOREFRONT&pf_rd_p=a9daf85d-aa24-446a-a1ca-2b67ade1a65b&pf_rd_r=VCQHQEXSGAY0B8BQ62YW&pd_rd_wg=TUP6C&pf_rd_s=merchandised-search-3&pf_rd_t=40901&ref_=dbs_f_r_shv_ts_a9daf85d-aa24-446a-a1ca-2b67ade1a65b_0&pd_rd_w=0mROC&pf_rd_i=116169071&pd_rd_r=e0146d6b-cb6a-4415-8cc7-017956870fa0"
try:
	kv = {'user-agent':'Chrome/10'}
	r = requests.get(url,headers=kv)
	r.raise_for_status()	#如果状态不是200,引发HTTPError异常
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("产生异常")
