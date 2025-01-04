# what-if-portfolio
This Python script simulates a stock portfolio based on historical investment data provided in a CSV file and reinvests dividends according to a predefined allocation.
This script get a CSV of data (example included).

# TL;DR

## Vars:
#### The default is that the amount is in NIS (Israeli new shekel), if the amount is in USD set:  
`amount_in_nis = False`

#### Define portfolio allocation
```
portfolio_allocation = {
    'IVV': 0.10,
    'TQQQ': 0.10,
    'QQQ': 0.05,
    'SOXL': 0.11,
    'SOXX': 0.09,
    'UPRO': 0.10,
    'DGRO': 0.07,
    'SCHD': 0.13,
    'BRK-B': 0.15,
    'VFMO': 0.10
}
```

#### The CSV shoult be like:
| Date       | Amount |
|------------|--------|
| 01/07/2019 | 2000   |
| 01/05/2020 | 1500   |
| 01/09/2022 | 1700   |
| 13/12/2023 | 2200   |
| 17/12/2024 | 2400   |  
  
.  
.  

# Not TL;DR
## Script Key Steps:

### Data Loading & Preparation:

Loads historical investment data from a CSV file (stocks_money_transfer_history.csv).
Standardizes column names and converts the date column into a proper datetime format.

### Portfolio Setup:

A fixed portfolio allocation is defined with specific percentage allocations for multiple stocks.
The script uses a static exchange rate of 3.5 NIS/USD for simplicity.

### Historical Data Fetching:

Downloads historical price and dividend data using yfinance.
Ensures missing market data is handled by checking the next available market day.

### Simulation Logic:

For each investment date, it calculates the amount invested based on the portfolio allocation.
Dividends Handling: Dividends are accumulated between investment dates and reinvested according to the portfolio allocation.

### Final Portfolio Calculation:

After processing all investments, the script calculates:
The final number of shares owned for each stock.
The last price for each stock.
The total USD value for each stock based on the last price.

### Results Export:

The final portfolio (including shares owned, last price, and USD value) is saved to a CSV file with a random number appended to avoid overwriting previous results.
The portfolio and total value are printed to the console.
