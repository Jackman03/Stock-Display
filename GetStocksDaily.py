#Program to return the trending stocks on the nasdaq
#Scrapes the data into a json file
#main program can either look at these stocks or a default stock list
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import GetPrice as Prices


#read in list of current stocks.
def GetTopStocks(StockLimit: int):
    URL = f'https://finance.yahoo.com/markets/stocks/most-active/?start=0&count={StockLimit}'

    r = requests.get(URL)

    soup = BeautifulSoup(r.text,'html.parser')
    StockTable = soup.find(class_='body yf-paf8n5')

   
    TrendingStocks = []
    StockList = Prices.LoadJson('StockList.json')

    for row in StockTable.find_all(class_='row false yf-paf8n5'):
         ticker = (row.find(class_='symbol yf-1m808gl').text).rstrip()

         if not CheckLists(StockList,ticker):
            Stock = ({"Ticker": (row.find(class_='symbol yf-1m808gl').text).rstrip(),
                       "Name": row.find(class_='tw-pl-4 yf-h8l7j7').text})
            TrendingStocks.append(Stock)

   


    with open('TrendingStocks.json' , 'w') as json_file:
            json.dump(TrendingStocks, json_file,indent=1)


def CheckLists(StockList, Ticker: str):
    #slow checking method...
    for Stock in StockList:
        if Stock['Ticker'] == Ticker:
            #print(f'{Ticker} is dupe')
            return True
    return False
        
         
    

#reset the list at market close
GetTopStocks(50)
