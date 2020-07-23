#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from voluptuous import Schema, Url
import os
import time
import sys

links = []

def createIndexPage():
    f = open("contents/index.html", 'w')
    for link in links:
        f.write('<a href="' + link + '">' + link + '</a><br>')
    f.close()

def saveContent(url):
    filename = url.split("/")[-1]
    links.append(filename)
    f = open("contents/" + filename, 'w')
    print(url)
    soup = BeautifulSoup(urlopen(url).read().decode('utf-8'), "html.parser")
    f.write(soup.find("article").prettify())
    f.close()

def parseContent(baseUrl, url):
    f = urlopen(url)
    soup = BeautifulSoup(f.read().decode('utf-8'), "html.parser")
    titles = soup.find("ul", attrs={"class": "contentsList"}).find_all("li")
    for title in titles:
        link = title.find("a").get("href")
        schema = Schema(Url())
        saveContent(schema(baseUrl + link))

    next = soup.find("a", attrs={"class": "pagingNext"})
    if next is not None:
        return baseUrl + next.get("href")
    else:
        return None

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("input ameblo id")
        sys.exit()
    amebloid = sys.argv[1]
    baseUrl = "http://ameblo.jp/" 
    url = baseUrl + amebloid + "/entrylist.html"
    try:
        os.mkdir("contents")
    except FileExistsError:
        pass
    while url is not None:
        url = parseContent(baseUrl, url)
        time.sleep(3)
    createIndexPage()
