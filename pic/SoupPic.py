#!/usr/bin/env python3
# Anchor extraction from HTML document
# import os
# os.environ["HTTPS_PROXY"] = "http://username:password@your-corporate-proxy.com:port"

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context

    html = urlopen('https://tieba.baidu.com/p/2555125530')
    bs = BeautifulSoup(html.read(), 'html.parser')
    tagAList = bs.find_all("img")

for link in tagAList:
    print(link.get('src'))
    # print(tagAList)
