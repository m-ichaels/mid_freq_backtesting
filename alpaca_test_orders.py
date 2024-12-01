from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockLatestQuoteRequest

KEY = 'PK1FSI37O17SE0J9Y7NF'
SECRET_KEY = 'eFKWe2hN771IBcH27mc7BJSNZNI5ecp6utRq7isd'
# paper=True enables paper trading
trading_client = TradingClient(KEY, SECRET_KEY, paper=True)
client = StockHistoricalDataClient(KEY, SECRET_KEY)

# multi symbol request - single symbol is similar
multisymbol_request_params = StockLatestQuoteRequest(symbol_or_symbols=["SPY", "GLD", "TLT"])

latest_multisymbol_quotes = client.get_stock_latest_quote(multisymbol_request_params)

gld_latest_ask_price = latest_multisymbol_quotes["GLD"].ask_price

# preparing orders
market_order_data = MarketOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.BUY,
                    time_in_force=TimeInForce.DAY
                    )

market_order_data2 = MarketOrderRequest(
                    symbol="SPY",
                    qty=1,
                    side=OrderSide.SELL,
                    time_in_force=TimeInForce.DAY
                    )

# Market order
#market_order = trading_client.submit_order(
#                order_data=market_order_data
#               )
