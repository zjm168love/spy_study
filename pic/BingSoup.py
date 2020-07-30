#!/usr/bin/env python3
# Anchor extraction from HTML document
# import os
# os.environ["HTTPS_PROXY"] = "http://username:password@your-corporate-proxy.com:port"
import re
import ssl
import time
import urllib
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def reqAndRetrieve(baseUrl, pageNumber):
    # 分页判断
    if pageNumber == 1:
        url = baseUrl
    else:
        url = baseUrl + '?p=' + str(pageNumber)

    print('base request url:' + url)
    req = Request(url=url, headers=headers)
    html = urlopen(req)
    bs = BeautifulSoup(html.read(), 'html.parser')

    divContainers = bs.find_all("div", class_="container")
    # divContainer.find_children()
    # items = bs.find_all("div", class_="item")

    picUrlList = getPicUrlLists(divContainers)

    _retrieve(picUrlList)


def _retrieve(picUrlList):
    for url in picUrlList:
        filename = url[7:-13]
        picUrl = "http://h1.ioliu.cn/bing" + url + "_1920x1080.jpg?imageslim"

        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0')
        opener.retrieve(picUrl, '/Users/pepchou/Desktop/study/架构师/python/soup/' + filename + ".jpg")
        time.sleep(1)


def getPicUrlLists(divContainersHtml):
    originUrlList = []
    for div in divContainersHtml:
        for item in div.find_all("div", class_="item"):
            pic_url = item.find("a").attrs["href"]
            originUrlList.append(pic_url)
    print(originUrlList)
    urlList = []

    for url in originUrlList:
        # urlList.append(url[6:-13])
        urlList.append(
            re.match('([a-zA-Z0-9_^.!-/]*)\?', url).group()[6:-1]
        )
    return urlList


if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    # str = re.match('([a-zA-Z0-9_^.!-]*)\?', "shshshshsh?234")
    # print(str.group())

    pageNumber = 1
    totalPageNumber = 5
    # baseUrl = "https://bing.ioliu.cn/"
    rankingUrl = "https://bing.ioliu.cn/ranking"
    while pageNumber <= totalPageNumber:
        reqAndRetrieve(rankingUrl, pageNumber)
        pageNumber = pageNumber + 1

    print('total pageNumber:' + str(pageNumber))
    print('completed')

    # .group()[:-1]
