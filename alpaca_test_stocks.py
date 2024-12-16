from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

# keys required for stock historical data client
client = StockHistoricalDataClient('your_alpaca_key_here', 'your_secret_key_here')

# multi symbol request - single symbol is similar
multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price

print(gld_latest_ask_price)