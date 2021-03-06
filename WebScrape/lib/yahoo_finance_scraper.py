#!/home/hadoop/anaconda3/bin/python3.7
from bs4 import BeautifulSoup
import urllib.request
import csv
import sys
def create_common_attributes(summarry,data_intervals,attr,data):   #Moving elements craped to  common output format


    for item in summarry:
        attr.append(item)
    for item in data_intervals:
        attr.append(item)
    del attr[2:13]
    attr[1], attr[2] = attr[2], attr[1]
    attr[3], attr[2] = attr[17].split("-")    
    
    attr[4], attr[7] = attr[7], attr[4]
    attr[9], attr[5] = attr[5], attr[9]
    attr[6]= attr[25].split('(')[0]
    attr[12], attr[7] = attr[7], attr[12]
    print(attr)

    attr[9], attr[8] = attr[17].split("-")
    attr[10] = "yf"
    attr[11] = data
    del attr[12:32]
    res = []
    for x in attr:
        res.append(x)
    return res

def yf_scrape(stock,data):


    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36')]
    response = opener.open('https://finance.yahoo.com/quote/'+stock)

    soup = BeautifulSoup(response, 'html.parser')
    price = soup.find ('h3',{'class':'intraday__price'})
    price = soup.find ('span',{'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
    #print(price)
    summarry = []
    summarry = soup.find_all('span',{'class':'Trsdu(0.3s)'}) 
    sumarry_list = []
    for i in summarry:
        sumarry_list.append(i.text)

    data_intervals = soup.find_all('td',{'class':'Ta(end) Fw(600) Lh(14px)'}) 
    data_intervals_list = []
    for i in data_intervals:
        data_intervals_list.append(i.text)
        
    summarry_atb = []
    summarry_atb.append(price.text)
    #summarry_atb.append(highlow.text)

    
    summarry_atb = create_common_attributes(sumarry_list,data_intervals_list,summarry_atb,data)
    return summarry_atb


