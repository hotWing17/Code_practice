#下载一整个页面所有套图

import requests
#引入正则表达式
import re
#引入文件操作库
import os
from bs4 import BeautifulSoup
import traceback

#获取URL的HTML内容
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        return r.text
    except:
        print('getHTMLText()出错！')

#从套图html内容解析出每张图片下载地址列表(url:该套图url)
def getPictureUrl_List(List, url):
    html = getHTMLText(url)
    try:
        #使用正则表达式匹配(使用最小匹配)
        #获得无数个该种（“big”:“XXX”）字符串的列表
        pcltDict = re.findall(r'"big":".*?\.jpg"', html)
        #将该列表转换为字符串
        html_real = "".join(pcltDict)
        #使用正则表达式匹配，获取真正可以用于下载的图片url列表
        pclt = re.findall(r'http://.*?\.jpg', html_real)
        for g in pclt:
            List.append(g)
    except:
        traceback.print_exc()
        print('getPictureUrl_List()出错!')

#循环下载每一张图片(List:该套图所有图片的url; path:为该套图保存文件夹的路径)
def downloadPicture(List, path):
    try:
        #判断主目录是否存在(不存在则创建目录)
        if not os.path.exists(path):
            os.mkdir(path)
        for i in range(len(List)):
            name = path + str(i+1) + '.jpg'
            if not os.path.exists(name):

                r = requests.get(List[i])
                with open(name, 'wb')as f:
                    f.write(r.content)
                print('\r第 ' + str(i+1) + ' 张图片成功下载！',end = '')
            else:
                print('文件已经存在')
        print('')
        print('')
    except:
        traceback.print_exc()
        print('downloadPicture()出错！')

#从首页获取单独套图的URL，返回一个列表
def getALLlist(T_list, T_url):
    html = getHTMLText(T_url)
    try:
        soup = BeautifulSoup(html, 'html.parser')
        #找到所有的a标签列表（包含该套图的url信息）
        A = soup.find_all('a',attrs={'class':'proimg'})
        #提取所有<a>标签中的[‘href’]属性的参数
        for a in A:
            url = T_url + a.attrs['href']
            T_list.append(url)
    except:
        traceback.print_exc()
        print('getALLlist()出错！')
    
#下载该页面所有套图方法!!!!!!!!!!!!!!!!!!!!!!!!!
def downloadALL(T_List, root):
    #存储一个套图所有图片的url
    try:
        #for i in range(len(T_List)):
        for i in range(15):
            List = []
            getPictureUrl_List(List, T_List[i])
            path = root + str(i+1)+'/'
            print('正在下载第' + str(i+1) + '个套图')
            downloadPicture(List, path)
    except:
        traceback.print_exc()
        print('')


def main():
    url = 'http://pic.yxdown.com'
    #root为所有套图都在装在该文件夹
    root = '/home/dc/桌面/爬虫练习(一)/图片/'
    #该列表存储所有套图的url
    T_list = []
    getALLlist(T_list, url)
    downloadALL(T_list, root)

main()
