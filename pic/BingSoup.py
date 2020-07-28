#!/usr/bin/env python3
# Anchor extraction from HTML document
# import os
# os.environ["HTTPS_PROXY"] = "http://username:password@your-corporate-proxy.com:port"
import time
import urllib

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import ssl

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    url = "https://bing.ioliu.cn/"
    req = Request(url=url, headers=headers)
    html = urlopen(req)
    bs = BeautifulSoup(html.read(), 'html.parser')

    divContainers = bs.find_all("div", class_="container")
    # divContainer.find_children()
    # items = bs.find_all("div", class_="item")

    originUrlList = []
    for div in divContainers:
        for item in div.find_all("div", class_="item"):
            pic_url = item.find("a").attrs["href"]
            originUrlList.append(pic_url)

    print(originUrlList)

    urlList = []
    for url in originUrlList:
        urlList.append(url[6:-13])

    for url in urlList:
        filename = url[7:-13]
        picUrl = "http://h1.ioliu.cn/bing" + url + "_1920x1080.jpg?imageslim"

        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0')
        opener.retrieve(picUrl, '/Users/pepchou/Desktop/study/架构师/python/soup/' + filename+".jpg")
        time.sleep(1)



    https://bing.ioliu.cn/?p=2
        # print(filename)
# for link in tagAList:
#     print(link.get('src'))
# print(tagAList)
