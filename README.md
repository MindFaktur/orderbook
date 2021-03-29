# orderbook
Places market orders on 15 minute timeframes based on ema strategy and places limit orders on 4hr time frame.

There are two functions defined namely market() and limit()

* Market function is scheduled to run every 15 minutes and calculate the 20 and 200ema.
* if 20 ema crosses above 200 ema it adds the quantity of bitcoin bought and the price at which it was bought to the market buys list.
* if 20 ema crosses below 200 ema it adds the quantity of bitcoin sold and the price at which it was sold to the market sell list.

* limit function is scheduled to run every 15 minutes and it just places orders based on pricce movement.
* if the current 4hr candle closes $100 above the previous 4hr candle then it places a limit buy order $100 below the current candle close.
* if the current 4hr candle closes $100 below the previous 4hr candle then it places a limit sell order $100 above the current candle close.
