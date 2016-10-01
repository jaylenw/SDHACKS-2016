import requests
from bs4 import BeautifulSoup
import re
import time

#scrapy

def fetchHTML(url):
    r = requests.get(url)
    code = r.status_code
    if code < 200 & code > 299:
        print("Code failed ")
        print (str(code))
        return
    print(url)
    return r.text

def parseHTML(text):
    soup = BeautifulSoup(text)
    title = str(soup.title)[7:]
    title = title[:len(title)-8]
    print(title)
    genre(soup.text)
    """
    x = re.split("span", soup.text, 10000000)
    length = len(x)
    for i in range(0, length):
        print(x[i])
        time.sleep(1)
    print("\n\n\n\n~~~~~~~~~~~diffffff")
    """
    x = re.findall(" [0-9]+\.[0-9][0-9]*", soup.text)
    avg = 0.0
    for i in range(0, len(x)):
        x[i] = float(str(x[i])[1:])
        avg += x[i]
    print(avg/len(x))


def genre(stuff):
    cuisine = {"SICILLIANI":"Italian", "Brewery":"General", "Fish & Chips":"General"}
    k = cuisine.keys()
    for i in range(0, len(k)):
        temp = re.findall(k[i], stuff)
        if len(temp) != 0:
            print(cuisine.get(k[i]))
            return

def scrape():
    txt = fetchHTML('http://www.zanzibarcafe.com/Loft-Lunch-Menu.html')
    parseHTML(txt)
    txt = fetchHTML('http://menu.rockbottom.com/la-jolla')
    parseHTML(txt)
    txt = fetchHTML('http://www.angelosandvincis.com/menus_dinner.html')
    parseHTML(txt)


scrape()
