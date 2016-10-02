import requests
from bs4 import BeautifulSoup
import re
import time
import json
#scrapy
for_json = {}
def fetchHTML(url):
    r = requests.get(url)
    code = r.status_code
    if code < 200 & code > 299:
        print("Code failed ")
        print (str(code))
        return
    for_json["url"] = url
    return r.text

def parseHTML(text):
    soup = BeautifulSoup(text)
    title = str(soup.title)[7:]
    title = title[:len(title)-8]
    for_json["name"] = title#print(title)
    genre(soup.text)
    x = re.findall(" [0-9]+\.[0-9][0-9]*", soup.text)
    avg = 0.0
    for i in range(0, len(x)):
        x[i] = float(str(x[i])[1:])
        avg += x[i]
    for_json["avgPrice"] =  avg/len(x)#print(avg/len(x))


def genre(stuff):
    cuisine = {"SICILLIANI":"Italian", "Huevos":"Mexican", "ANGUS":"General", "Brewery":"General", "Fish & Chips":"General"}
    k = cuisine.keys()
    for i in range(0, len(k)):
        temp = re.findall(k[i], stuff)
        if len(temp) != 0:
            for_json["category"] = cuisine.get(k[i])#print(cuisine.get(k[i]))
            return

def scrape():
    f = open("data.json", "w")
    txt = fetchHTML('http://www.zanzibarcafe.com/Loft-Lunch-Menu.html')
    parseHTML(txt)
    f.write("{")
    val = 0
    for (k,v) in for_json.items():
        f.write(str(k)+":"+str(v))
        if val != len(for_json)-1:
            f.write(",")
            val += 1
    f.write("},")
    txt = fetchHTML('http://menu.rockbottom.com/la-jolla')
    parseHTML(txt+",")
    f.write("{")
    val = 0
    for (k,v) in for_json.items():
        f.write(str(k)+":"+str(v))
        if val != len(for_json)-1:
            f.write(",")
            val += 1
    f.write("},")
    txt = fetchHTML('http://www.angelosandvincis.com/menus_dinner.html')
    parseHTML(txt)
    f.write("{")
    val = 0
    for (k,v) in for_json.items():
        f.write(str(k)+":"+str(v))
        if val != len(for_json)-1:
            f.write(",")
            val += 1
    f.write("}")
    txt = fetchHTML('http://www.theshoresrestaurant.com/Menus/Lunch')
    parseHTML(txt)
    f.write("{")
    val = 0
    for (k,v) in for_json.items():
        f.write(str(k)+":"+str(v))
        if val != len(for_json)-1:
            f.write(",")
            val += 1
    f.write("}")
    txt = fetchHTML('http://www.greatmexgrill.com/')
    parseHTML(txt)
    f.write("{")
    val = 0
    for (k,v) in for_json.items():
        f.write(str(k)+":"+str(v))
        if val != len(for_json)-1:
            f.write(",")
            val += 1
    f.write("}")
    f.close()


scrape()
