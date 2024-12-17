# README

## Purpose

This repository demonstrates my proficiency in Python programming and my ability to design and implement trading algorithms using real-world financial data. The code here is intended to showcase my skills, including working with APIs, performing data analysis, and backtesting trading strategies. While the algorithms are functional and follow common trading principles, the main objective of this project is to illustrate my knowledge and expertise in creating Python-based financial models.

## Files Overview

### 1. **Stock Trading Algorithm (Alpaca API)**  
   - **Purpose**: This script fetches historical stock data using the Alpaca API, calculates technical indicators like the RSI (Relative Strength Index), and uses them to make buy/sell decisions. 
   - **Backtest**: It simulates trades with a simple strategy based on RSI values and keeps track of the portfolio performance, including equity curve, trade log, and metrics such as maximum drawdown and win percentage.

### 2. **Crypto Trading Algorithm (Binance API)**  
   - **Purpose**: This script downloads cryptocurrency price data from the Binance API and performs a backtest using a trading strategy based on the RSI indicator. It uses multiple buy thresholds, profit-taking levels (TP), and stop-loss (SL) percentages.
   - **Backtest**: The algorithm tracks the account’s performance and calculates key metrics like ROI, win rate, drawdown, and profit/loss from each trade. It also includes logic for dynamic position sizing based on various RSI levels.

## Key Features
- **RSI Calculation**: Both scripts calculate RSI, a widely used momentum indicator in technical analysis.
- **Portfolio Management**: The scripts manage cash and positions, tracking the number of shares or crypto assets held and performing buy/sell actions based on strategy rules.
- **Backtesting**: The backtest logic simulates historical trading, providing performance metrics such as profit/loss, win rate, and drawdown.
- **Data Fetching**: The scripts fetch historical stock and cryptocurrency data from the Alpaca and Binance APIs, respectively.
- **Trade Log**: A log of all executed trades is kept for review, helping to track the decision-making process.

## How It Works
- **Alpaca API**: The first script uses the Alpaca API to get stock data (GLD) and apply an RSI-based strategy. It simulates trades, calculates portfolio performance, and provides insights into the strategy’s effectiveness.
- **Binance API**: The second script fetches cryptocurrency data (e.g., QNT/USDT) and uses the RSI indicator along with specific thresholds for buying, selling, and stop-loss management. It tracks the results and evaluates the strategy's performance over a given timeframe.

## Disclaimer
- **Educational Purposes**: The algorithms and strategies in this repository are designed for educational purposes to demonstrate my understanding of Python programming, algorithmic trading, and data analysis. They should not be used for real-world trading without significant adjustments and additional risk management.
  
- **Not Financial Advice**: This repository does not provide financial advice, nor should it be interpreted as such. Use these scripts at your own risk.

## Future Improvements
- **Strategy Refinement**: The algorithms could be expanded to include more advanced trading strategies, better risk management, and automated live trading capabilities.
- **More Indicators**: Additional technical indicators and machine learning models could be integrated for more robust decision-making.
- **Optimization**: The code can be optimized for better performance and accuracy, especially in terms of backtesting speed and real-time data fetching.

## Conclusion
This repository is a showcase of my ability to design and backtest trading strategies using Python. My aim is to demonstrate my understanding of algorithmic trading, data handling, and performance analysis to potential employers. Please feel free to explore the code, adapt it, or use it as a reference for your own projects.

---

If you have any questions or suggestions, feel free to open an issue or contact me directly.