from bs4 import BeautifulSoup
import urllib.request
import csv
import sys

stock = sys.argv[1]

#atributes of stock
attributes = ["Price","Open", "High","Low","MarketCap","Racio","Dividend","Close","High52","Close52"]

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36')]
response = opener.open('https://www.google.com/search?q='+stock)

soup = BeautifulSoup(response, 'html.parser')
price = soup.find ('span',{'class':'IsqQVc NprOob XcVN5d'})
summarry = soup.find_all('td',{'class':'iyjjgb'}) 
summarry_atb = price

with open(stock+'_googlefinance.csv','w', newline='') as file:
    writer = csv.writer(file,delimiter="\t")
    writer.writerow(attributes)
    #writer.writerow(price)
    for item in summarry:
       summarry_atb.append(item.text)
    writer.writerow(summarry_atb)
file.close()