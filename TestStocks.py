#Demo file to test stocks
#idea is to get the top 50 stocks for the day and display them
import GetPrice as Prices
import GetStocksDaily as Daily
import time
Stocks = Prices.LoadJson('StockList.json')
Daily.GetTopStocks(25)
TrendingStocks = Prices.LoadJson('TrendingStocks.json')


for stock in TrendingStocks:
    #time.sleep(1)
    curStock = stock['Ticker']
    print(f' {curStock} - {Prices.GetCurrentPrice(curStock)}')

for stock in Stocks:
    #time.sleep(1)
    curStock = stock['Ticker']
    print(f' {curStock} - {Prices.GetCurrentPrice(curStock)}')
