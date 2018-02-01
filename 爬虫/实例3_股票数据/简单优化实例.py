#股票数据定向爬虫
#优化：r.apparent_encoding是需要解析整个页面之后才可以返回值的，所以可以在参数里面
#优化：打印当前打印进度条的百分比('\r':将打印的字符串的光标提到这一行的头部，下一行打印的时候就会覆盖这一行的内容)
import requests
from bs4 import BeautifulSoup
import traceback    #为了调试方便
import re

def getHTMLText(url, code = 'utf-8'):		#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #获取url页面信息
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = code					#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return r.text
    except:
        return ""

def getStockList(lst, stockURL):
    #获取全部股票列表信息(参数‘lst’:个股存储的列表'、'stockURL':获取股票列表的网站)
    html = getHTMLText(stockURL, 'GB2312')	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    #找到所有<a>标签
    for i in a:
        #获取<a>标签中'href'属性的值，并且将股票代码提取出来，存入lst列表中
        try:
            href = i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}', href)[0])
        except:
            continue

def getStockInfo(lst, stockURL, fpath):
    count = 0
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    #获取个股信息，并保存到文件(参数‘lst’:保存股票的列表、'stockURL':获取个股信息的网站、'fpath':保存文件地址)
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            #定义一个字典，用来存储从个股页面返回全部信息
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
    	    #找到关于个股信息的标签(自己查阅源代码发现的位置)

            name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
    	    #在个股标签下找到个股名称标签
            infoDict.update({'股票名称': name.text.split()[0]})
    	    #找到'个股名称标签'的string值用空格符分开(舍弃名称后面的一些字符)，之后更新到字典中去

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
                #字典的赋值方法
                #打开目标文件，进行写操作
            with open(fpath,'a',encoding = 'utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print('\r当前速度：{:2f}%'.format(count*100/len(lst)),end = '')
                #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        except:
            count = count + 1
            print('\r当前速度：{:2f}%'.format(count*100/len(lst)),end = '')
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            #出错时可以获得出错的信息continue

def main():
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = '/home/dc/桌面/爬虫/实例3_股票数据/BaiduStockIofo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    #获取股票列表信息
    getStockInfo(slist, stock_info_url, output_file)
    #使用股票列表信息，获取个股信息，并保存到指定文件中

main()

















    
