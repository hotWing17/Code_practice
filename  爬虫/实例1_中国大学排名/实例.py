import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):   #将页面放到列表中‘ulist’
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:          #遍历‘tbody’标签的孩子
        if isinstance(tr,bs4.element.Tag):          #此语句为了排除非Tag标签
            TD = tr.find('td')                      #tbody下有一个大’td‘标签，里面包含多个小’td‘标签
            tds = TD('td')                          #将所有'td'标签存入 列表’tds‘
            ulist.append([TD.contents[0],tds[0].div.string,tds[2].string])                       #append()在列表中加入值(大学名字，排名，总分)
    #pass                        #不做任何操作的语句（写框架的时候使用）

def printUnivList(ulist,num):
    print("{:^10}\t{:^15}\t{:^15}".format("排名","学校名称","总分"))     #打印表头
    for i in range(num):
        u = ulist[i]
        print("{:^10}\t{:^15}\t{:^15}".format(u[0],u[1],u[2]))       #使用和表头的字符串格式

def main():
    uinfo = []                  #将大学信息放到该列表中
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2017.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20)     #20 univs
main()

















    
