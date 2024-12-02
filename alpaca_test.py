from alpaca.data.historical import CryptoHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime

# no keys required for crypto data
client = CryptoHistoricalDataClient()

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD", "ETH/USD"],
                        timeframe=TimeFrame.Day,
                        start=datetime(2022, 7, 1),
                        end=datetime(2022, 9, 1)
                 )

bars = client.get_crypto_bars(request_params)

btc_data = bars.df.loc["BTC/USD"]

periods=14
delta = btc_data['open'].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=periods, min_periods=1).mean()
avg_loss = loss.rolling(window=periods, min_periods=1).mean()

rs = avg_gain / avg_loss

rsi = 100 - (100/(1 + rs))
print(rsi)
# print(rsi.iloc[-1])