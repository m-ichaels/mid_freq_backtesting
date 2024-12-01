import requests
import matplotlib.pyplot as plt
import pandas as pd

url = "https://data.alpaca.markets/v2/stocks/bars"

headers = {
    "accept": "application/json",
    "APCA-API-KEY-ID": "PK1FSI37O17SE0J9Y7NF",
    "APCA-API-SECRET-KEY": "eFKWe2hN771IBcH27mc7BJSNZNI5ecp6utRq7isd",
}

params = {
    "symbols": "SPY",
    "timeframe": "30Min"
}

response = requests.get(url, headers=headers, params=params)

data = response.json()
spy_data = data['bars']['SPY']
df = pd.DataFrame(spy_data)
print(df['c'])



# print(response.text)

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