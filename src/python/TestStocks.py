#Demo file to test stocks
#idea is to get the top 50 stocks for the day and display them
import GetPrice as Prices
import GetStocksDaily as Daily
Stocks = Prices.LoadJson('src/data/StockList.json')
#Daily.GetTopStocks(25)
#TrendingStocks = Prices.LoadJson('src/data/TrendingStocks.json')


for stock in Stocks:
    #time.sleep(1)
    curStock = stock['Ticker']
    print(f' {curStock} - {Prices.GetCurrentPrice(curStock)}')
