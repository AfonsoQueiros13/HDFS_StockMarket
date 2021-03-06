
from bs4 import BeautifulSoup
import urllib.request
import csv
import sys
def create_common_attributes(summarry, attr,data):   #Moving elements craped to  common output format
    for item in summarry:
        attr.append(item)
    del attr[2:7]
    attr[1], attr[3] = attr[3], attr[2]
    attr[2], attr[5] = attr[5], attr[2]
    attr[2], attr[3] = attr[2].split("-")
    attr[2], attr[3] = attr[3], attr[2]
    attr[6], attr[4] = attr[4], attr[6]
    attr[11], attr[5] = attr[5], attr[11]
    attr[14], attr[6] = attr[6], attr[14]
    attr[1], attr[11] = attr[11], attr[1]
    attr[11], attr[7] = attr[7], attr[11]
    attr[14], attr[15] = attr[14].split("-")
    attr[14], attr[2] = attr[2], attr[14]
    attr[15], attr[3] = attr[3], attr[15]
    attr[14], attr[8] = attr[8], attr[14]
    attr[15], attr[9] = attr[9], attr[15]
    attr[10] = "mktw"
    attr[11] = data
    del attr[12:19] 
    res = []
    for x in attr:
        res.append(x)
    return res

def mktw_scrape(stock,data):




    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36')]
    response = opener.open('https://www.marketwatch.com/investing/stock/'+stock)

    soup = BeautifulSoup(response, 'html.parser')
    price = soup.find ('bg-quote',{'class':'value'})
    close = soup.find ('td',{'class':'table__cell u-semi'})
    summarry = soup.find_all('span',{'class':'primary'}) 
    sumarry_list = []
    for i in summarry:
        sumarry_list.append(i.text)
    #Scraping of values that dont appear with the same class as the other indicators
    summarry_atb = []
    summarry_atb.append(price.text) 
    summarry_atb.append(close.text)

    summarry_atb = create_common_attributes(sumarry_list, summarry_atb,data)
    print(summarry_atb)
    return summarry_atb
