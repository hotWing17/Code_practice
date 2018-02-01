#因为商品页面的信息可以直接通过搜索获取信息，则可以不需要使用BeautifulSoup库

import requests
import re

def getHTMLText(url):
    #获取html页面信息
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    #html为输入参数，将商品价格和名称提取出来，放到ilt这个列表里面
    try:
        #findall(),split(),eval()都可能出现问题，使用try避免程序退出
        plt = re.findall(r'"view_price":"[\d\.]*"',html)
        tlt = re.findall(r'"raw_title":".*?"',html)
        #使用正则表达式进行匹配
        for i in range(len(plt)):
            #for循环将匹配到的字符串进行提取，将信息赋值给列表
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("")

def printGoodsList(ilt):
    #输出全部商品的信息
    tplt = "{:4}\t{:8}\t{:16}"
    #约定输出格式
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods = "书包"
    depth = 2
    #爬取深度为2页
    start_url = "https://s.taobao.com/search?q=" + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url +'&s=' + str(44*i)
            #翻页操作
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()
