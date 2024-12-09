#Demo file to test stocks
import GetPrice as Prices
import time
Stocks = Prices.LoadJson('StockList.json')
for stock in Stocks:
    time.sleep(1)
    curStock = stock['Ticker']
    print(f' {curStock} - {Prices.GetCurrentPrice(curStock)}')