#下载一整套的图片

import requests     #引入文件操作库
import os
import traceback    #为调试方便
import re           #引入正则表达式

#获取套图html的内容
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status
        return r.text
    except:
        print('getHTMLText()出错！')

#获取套图每一张图片的url
def getPictureUrl_List(List, html):
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
        print('getPictureUrl_List()出错！')

#下载图片到目标路径
def downloadPicture(List, root):
    try:
        #判断主目录是否存在(不存在则创建目录)
        if not os.path.exists(root):
            os.mkdir(root)
        for i in range(len(List)):
            name = root + str(i+1) + '.jpg'
            if not os.path.exists(name):

                r = requests.get(List[i])
                with open(name, 'wb')as f:
                    f.write(r.content)
                print('\r第 ' + str(i+1) + ' 张图片成功下载！',end = '')
            else:
                print('文件已经存在')
    except:
        traceback.print_exc()
        print('downloadPicture()出错！')

    
    print('')

def main():
    #目标网页的URL
    url = 'http://pic.yxdown.com/html/7888.html#p=10'
    #创建一个列表(存放所有图片的下载url)
    List = []
    #图片的存放路径
    path = '/home/dc/桌面/爬虫练习(一)/图片/'
    html = getHTMLText(url)
    getPictureUrl_List(List, html)
    downloadPicture(List, path)

main()
