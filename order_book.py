

import time
import schedule

import pandas as pd
import requests




market_sells = []
market_buys = []
limit_buys = []
limit_sells = []



def market():

    url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=15m&limit=1000'

    df = pd.DataFrame(requests.get(url).json())
    df.rename(columns={0: 'DATE', 1: 'OPEN', 2: 'HIGH', 3: 'LOW', 4: 'CLOSE', 5: 'VOLUME', 6: 'CLOSE_TIME',
                       7: 'Quote asset volume', 8: 'Number of trades', 9: 'Taker buy base asset volume',
                       10: 'Taker buy quote asset volume', 11: 'IGNORE'}, inplace=True)
    df = df.drop(columns=['DATE', 'VOLUME', 'CLOSE_TIME', 'Quote asset volume', 'Number of trades',
                          'Taker buy base asset volume',
                          'Taker buy quote asset volume', 'IGNORE'])
    ema_20 = list(df['CLOSE'].ewm(span=20).mean())

    ema_200 = list(df['CLOSE'].ewm(span=200).mean())


    if ema_20[-3]<ema_200[-3]:
        if ema_20[-2]>ema_200[-2]:
            closed = list(df['CLOSE'])
            order =  market_buys.append(' 0.05 ' + closed[-1])
    elif ema_20[-3]>ema_200[-3]:
        if ema_20[-2]<ema_200[-2]:
            closed = list(df['CLOSE'])
            order =  market_sells.append(' 0.05 ' + closed[-1])
    


def limits():
    url = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=4h&limit=1000'

    df = pd.DataFrame(requests.get(url).json())
    df.rename(columns={0: 'DATE', 1: 'OPEN', 2: 'HIGH', 3: 'LOW', 4: 'CLOSE', 5: 'VOLUME', 6: 'CLOSE_TIME',
                       7: 'Quote asset volume', 8: 'Number of trades', 9: 'Taker buy base asset volume',
                       10: 'Taker buy quote asset volume', 11: 'IGNORE'}, inplace=True)
    df = df.drop(columns=['DATE', 'VOLUME', 'CLOSE_TIME', 'Quote asset volume', 'Number of trades',
                          'Taker buy base asset volume',
                          'Taker buy quote asset volume', 'IGNORE'])

    closed = df['CLOSE']
    if closed[-2]>(closed[-3] + 100):
        limit_buys.append( ' 0.05 ' + ' at ' + (closed[-2] - 100) )
    if closed[-2]<(closed[-3] - 100):
        limit_sells.append(' 0.05 ' + ' at ' + (closed[-2] + 100) )



schedule.every(5).minutes.do(market)
schedule.every(4).hours.do(limits)

while True:
    schedule.run_pending()
    time.sleep(1)
