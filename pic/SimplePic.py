# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:31:25 2019
@author: sunst&晴雨qy
@des：爬取图片，提供两种方法
"""

# re模块主要包含了正则表达式
import re
# urllib模块提供了读取Web页面数据的接口
import urllib.request
from urllib import request
import ssl


# 定义一个getHtml()函数
def getSuperHtmlCode(url):
    print('start-getsuperhtml')
    ssl._create_default_https_context = ssl._create_unverified_context

    with request.urlopen(url) as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))
        return data


# 定义一个getHtml()函数
def getHtml(url):
    print('start-gethtml')
    page = urllib.request.urlopen(url)  # urllib.request.urlopen()方法用于打开一个URL地址
    html = page.read()  # read()方法用于读取URL上的数据
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'  # 正则表达式，得到图片地址
    imgre = re.compile(reg)  # re.compile() 可以把正则表达式编译成一个正则表达式对象.
    html = html.decode('utf-8')  # python3
    print('----------------------')
    print(html)
    imglist = re.findall(imgre, html)  # re.findall() 方法读取html 中包含 imgre（正则表达式）的数据
    # 把筛选的图片地址通过for循环遍历并保存到本地
    # 核心是urllib.request.urlretrieve()方法,直接将远程数据下载到本地，图片通过x依次递增命名
    x = 0

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '/Users/pepchou/Desktop/study/架构师/python/spy/%s.jpg' % x)
        x += 1


# html = getHtml("https://tieba.baidu.com/p/2555125530")
if __name__ == "__main__":
    html = getSuperHtmlCode("https://tieba.baidu.com/p/2555125530")
    print(html)
    print(getImg(html))
