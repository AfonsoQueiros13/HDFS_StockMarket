from bs4 import BeautifulSoup
import urllib.request
import csv
import sys
import datetime


def create_common_attributes(summarry,key_data,attr):   #Moving elements craped to  common output format
   for item in summarry:
      attr.append(item.text)
   for item in key_data:
      attr.append(item.text)
   attr.pop(1)
   
   for item in summarry:
      attr.append(item.text)
   #del attr[2:7]
   attr[1], attr[5] = attr[5], attr[1]
   #attr[2], attr[5] = attr[5], attr[2]
   attr[2], attr[3] = attr[4].split("-")
   attr[4], attr[9] = attr[9], attr[4]
   attr[7], attr[5] = attr[5], attr[7]
   attr[5]= attr[5].split('(')[0]
   attr[13], attr[6] = attr[6], attr[13]
   attr[6]= attr[6].split('(')[0]
   attr[24], attr[7] = attr[7], attr[24]
   attr[7]= attr[7].split('(')[0]
   attr[9], attr[8] = attr[9].split("-")
   del attr[10:25]
   
   return attr



def wsj_scrape(stock):
   now = datetime.datetime.now()
   data = now.strftime("%Y-%m-%d")


   #atributes of stock
   attributes = ["Price","Open", "High","Low","MarketCap","PERatio","Dividend","Close","High52","Low52"]

   opener = urllib.request.build_opener()
   opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36')]
   response = opener.open('https://www.wsj.com/market-data/quotes/'+stock)

   soup = BeautifulSoup(response, 'html.parser')
   #price = soup.find ('h3',{'class':'intraday__price'})
   price = soup.find ('span',{'id':'quote_val'})
   summarry = soup.find_all('span',{'class':'WSJTheme--data_data--2QuzEiZE'}) 
   key_data = soup.find_all('span',{'class':'WSJTheme--data_data--3CZkJ3RI'}) 
   summarry_atb = []
   summarry_atb.append(price.text)


   with open('scraping_wsj/'+ data + '_'+ stock +'_thewallstreet.csv','w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(attributes)
      summarry_atb = create_common_attributes(summarry,key_data,summarry_atb)
      writer.writerow(summarry_atb)
   file.close()