import requests
import matplotlib.pyplot as plt
import pandas as pd

url = "https://data.alpaca.markets/v2/stocks/bars"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": "your_alpaca_key_here",
    "APCA-API-SECRET-KEY": "your_secret__key_here",
}

sp500_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'BRK.B', 'V', 'JNJ', 'SPY']

params = {
    "symbols":"SPY",
    "timeframe":"5Min"
}

response = requests.get(url, headers=headers, params=params)

data = response.json()
spy_data = data['bars']['SPY']
periods = 14
df = pd.DataFrame(spy_data)

delta = df['c'].diff()

gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=periods, min_periods=1).mean()
avg_loss = loss.rolling(window=periods, min_periods=1).mean()

rs = avg_gain / avg_loss

rsi = 100 - (100/(1 + rs))
print(rsi.iloc[-1])

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()
    
#     # Extract the SPY data from the response
#     spy_data = data['bars']['SPY']
    
#     # Convert the data to a DataFrame for easier manipulation
#     df = pd.DataFrame(spy_data)
    
#     # Convert the timestamp to a datetime format
#     df['t'] = pd.to_datetime(df['t'])
    
#     # Plot the closing prices over time
#     plt.figure(figsize=(10, 6))
#     plt.plot(df['t'], df['c'], label='SPY Close Price')
#     plt.xlabel('Time')
#     plt.ylabel('Close Price')
#     plt.title('SPY Close Price Over Time')
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
    
# else:
#     print("Error:", response.text)