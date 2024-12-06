#New method using the Unoffical Yahoo Finance API
import requests
import time


def printDebug(r: requests):
    print(f'Status code: {r.status_code}')
    RetryTime = r.headers.get('Retry-After')
    print(f'Retry time: {RetryTime}')


def GetCurrentPrice(ticker):

    #For header retry time
    MAX_RETRIES = 3

    #Request headers from curl
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    #'Referer': 'https://finance.yahoo.com/quote/VOO/',
    'Origin': 'https://finance.yahoo.com',
    'Connection': 'keep-alive',
    # 'Cookie': 'A1=d=AQABBA00HGcCEOHG59q07KDrl0Jr579gNtgFEgEBCAHgN2djZ9ww0iMA_eMBAAcIDTQcZ79gNtg&S=AQAAAru2p3JiG9V4KhKHV4mOZFw; A3=d=AQABBA00HGcCEOHG59q07KDrl0Jr579gNtgFEgEBCAHgN2djZ9ww0iMA_eMBAAcIDTQcZ79gNtg&S=AQAAAru2p3JiG9V4KhKHV4mOZFw; PRF=t%3DVOO%252B%255EDJI%252B%255EGSPC; cmp=t=1732659039&j=0&u=1YNN; axids=gam=y-AF9kl2JE2uJur8IL8jjkFekIrAg4Q.2a~A&dv360=eS1NcE1EYWx4RTJ1Rjc4WFRRQ2lsdFg2WFZlSk1KanRLeX5B&ydsp=y-CUEftWdE2uIZsV5w9meZhko25NOX2VuI~A&tbla=y-5lhkd0VE2uJ8gHR_bkSsJ_5Yp0JZjtmR~A; GUC=AQEBCAFnN-BnY0Ii4QTl&s=AQAAAOuBDqGw&g=ZzadPA; A1S=d=AQABBA00HGcCEOHG59q07KDrl0Jr579gNtgFEgEBCAHgN2djZ9ww0iMA_eMBAAcIDTQcZ79gNtg&S=AQAAAru2p3JiG9V4KhKHV4mOZFw; gpp=DBABLA~BVRqAAAAAmA.QA; gpp_sid=7',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'DNT': '1',
    'Sec-GPC': '1',
    'Priority': 'u=4',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
    }

    #Requests
    r = requests.get(
        f'https://query2.finance.yahoo.com/v8/finance/chart/{ticker}?period1=1732143600&period2=1732662000&interval=1m&includePrePost=true&events=div%7Csplit%7Cearn&&lang=en-US&region=US',
        #cookies=cookies,
        headers=headers,
    )
    #Error checking

    match r.status_code:
        case 200:
            printDebug(r)

            #dump json
            data = r.json()
            curprice = data['chart']['result'][0]['meta']['regularMarketPrice']
            lastchange = data['chart']['result'][0]['meta']['previousClose']

            amtchange = curprice - lastchange

            amtchange = round(amtchange,2)

            perChange = round(((curprice - lastchange) / curprice) * 100,2)

            print(curprice)

            print(perChange)

            print(amtchange)

            return curprice,perChange,amtchange
    
        #WIP
        #Too many requests error
        case 429:
            #Allow the max amount of retries
            for retries in range(0,MAX_RETRIES):
            #Get "Retry-After" header
                RetryTime = r.headers.get('Retry-After')

                #Calculate the wait time
                if isinstance(RetryTime,(int, float)):
                    WaitTime = int (RetryTime)
                else:
                    #Exponential backoff
                    WaitTime = retries * MAX_RETRIES
                time.sleep(WaitTime)

        #WIP
        #Page not found error
        case 404:
            #One possible issue is the stock name is in all lowercase. so we
            print('404 error')

   

GetCurrentPrice('SPY')


