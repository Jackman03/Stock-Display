#jackson Vaughn
#Program to display data on the LCD screen
#!/usr/bin/env python3

#Imports
import time 
import LCDDriver as LCD    
from datetime import datetime
from GetPrice import *
from GetStocksDaily import *


def DisplayPrice(Ticker: str):
    #Screen cannot fit all 1 values so we will just display the ticker and current price. Guess I just need to buy a bigger display...
    PriceData= GetCurrentPrice(Ticker)

    #Prints out to the console for debugging
    print(f'{Ticker} - {PriceData}')

    #debug network issues here. The "issuses" are not really debugged in the GetPrice file just more logged

    match PriceData[1][0]:
        case 200:
        #Run each stock for 5 seconds
            for v in range(0,5):
                LCD.write(f'{Ticker} - ${PriceData[0][0]}' ,LCD.LINE_1)
                now = datetime.now()
                CurTime = str(now.strftime('%m-%d %H:%M:%S'))
                LCD.write(CurTime,LCD.LINE_2)
                time.sleep(1)
            return

        case 404:
            LCD.write(f'{Ticker} - {PriceData[1][0]}',LCD.LINE_1)
            LCD.write(f'invalid ticker',LCD.LINE_2)
            time.sleep(10)
            return
             
        case _:
            LCD.write(f'{Ticker} - {PriceData[1][0]}',LCD.LINE_1)
            LCD.write(f'{PriceData[1][2]}',LCD.LINE_2)
            time.sleep(10)
            return
        


#Basic function to setup the LCD
def main():
    #Boot up the list of stocks
    StockList = LoadJson('src/data/StockList.json')

    #So this doesn't work.
    #We need to redo the web scraping of the trending stocks page to keep it updated when market opens
    #GetTopStocks()
    TrendingStocks = LoadJson('src/data/TrendingStocks.json')

    #Setup LCD display
    LCD.setup()
    LCD.clear()
    
    #Print out starttime
    now = datetime.now()
    StartTime = str(now.strftime('%m-%d %H:%M:%S'))
    print(f'Starting at: {StartTime}')
    MarketOpen = datetime.strptime("9:30:00","%H:%M:%S").time()
    MarketClose = datetime.strptime("16:00:00","%H:%M:%S").time()
    
    while True:


        #Will loop from 09:30 to 16:30
        Curtime = datetime.now().time()
        CurDay = datetime.now().weekday()
        #format the market open time
        
        try:

            if Curtime >= MarketOpen and Curtime <= MarketClose and CurDay not in [5,6]:
                for stock in StockList:
                    CurStock = stock['Ticker']
                    DisplayPrice(CurStock)
                #Loop through the trending stocks. Need to fix the function that pulls them...
                for stock in TrendingStocks:
                    CurStock = stock['Ticker']
                    DisplayPrice(CurStock)
                #After each run refresh the list
                #GetTopStocks()

            else:
                LCD.clear()
                LCD.write('Market closed',LCD.LINE_1)
            
                
        except KeyboardInterrupt:
            print('User exited the program')
            LCD.clear()
            
            #Goodbye screen. Countdown from 5 
            for x in range(5,0,-1):
                LCD.write('Exit key pressed',LCD.LINE_1)
                LCD.write(f'Goodbye! {x}',LCD.LINE_2)
                time.sleep(1)
            LCD.clear()
            return

if __name__ == '__main__':
    main()
