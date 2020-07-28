#!/usr/bin/env python3
# Anchor extraction from HTML document
# import os
# os.environ["HTTPS_PROXY"] = "http://username:password@your-corporate-proxy.com:port"

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == "__main__":
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.html)
