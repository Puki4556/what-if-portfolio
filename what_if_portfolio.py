import pandas as pd
import yfinance as yf
import datetime
import time
import random

# Change values below
######################################################################
# Set currency type, default to NIS
# Set to False if the amount in the csv is in USD
amount_in_nis = True

# Define portfolio allocation
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

# Load your investment data
investment_data = pd.read_csv('stocks_money_invest_history.csv')
######################################################################

# Check for column names and standardize them
investment_data.columns = investment_data.columns.str.strip()

# Rename the 'Amount' column to 'Amount' if present
if 'Amount' in investment_data.columns:
    investment_data.rename(columns={'Amount': 'Amount'}, inplace=True)

# Verify column names
if 'Amount' not in investment_data.columns:
    raise ValueError("The column 'Amount' is not found in the CSV file. Available columns: " + str(investment_data.columns))

investment_data['Date'] = pd.to_datetime(investment_data['Date'], dayfirst=True)

# Fetch historical stock data and currency rates
assets = list(portfolio_allocation.keys())
stock_data = yf.download(assets, start=investment_data['Date'].min(), end=datetime.datetime.now(), group_by='ticker', actions=True)

# Prepare the simulation
simulation_results = []
final_portfolio = {stock: 0 for stock in portfolio_allocation.keys()}

# Use a static exchange rate fallback
static_usd_ils_rate = 3.5  # Approximate static rate, adjust as needed

# Helper function to find the next valid market day
def get_next_valid_market_day(stock, date):
    max_attempts = 5
    for _ in range(max_attempts):
        try:
            stock_price = stock_data[stock].loc[date]['Close']
            return stock_price
        except KeyError:
            date = (datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    raise ValueError(f"No valid market data found for {stock} starting from {date}")

for idx, row in investment_data.iterrows():
    date = row['Date'].strftime('%Y-%m-%d')
    amount = row['Amount']
    amount_in_usd = amount / static_usd_ils_rate if amount_in_nis else amount

    # Determine the next investment date or the end of the dataset
    next_date = investment_data.iloc[idx + 1]['Date'].strftime('%Y-%m-%d') if idx + 1 < len(investment_data) else datetime.datetime.now().strftime('%Y-%m-%d')

    # Accumulate dividends between current and next investment date
    total_dividends = 0
    for stock in portfolio_allocation.keys():
        dividends_in_range = stock_data[stock].loc[date:next_date]['Dividends'].sum()
        total_dividends += dividends_in_range * final_portfolio[stock]

    # Reinvest dividends using the allocation
    for stock, weight in portfolio_allocation.items():
        invested_amount = amount_in_usd * weight + (total_dividends * weight)
        try:
            stock_price = get_next_valid_market_day(stock, date)
            shares_bought = invested_amount / stock_price
            final_portfolio[stock] += shares_bought
        except KeyError:
            print(f"Missing data for {stock} starting from {date}")

# Add last price and USD value to the final portfolio
final_portfolio_data = []
total_portfolio_value = 0
for stock, shares_owned in final_portfolio.items():
    last_price = stock_data[stock].iloc[-1]['Close']
    usd_value = shares_owned * last_price
    total_portfolio_value += usd_value
    final_portfolio_data.append([stock, shares_owned, last_price, usd_value])

# Generate a random number to avoid overwriting
random_number = random.randint(1000, 9999)
final_portfolio_filename = f'final_portfolio_{random_number}.csv'

# Save the final stock amounts to a CSV file
final_portfolio_df = pd.DataFrame(final_portfolio_data, columns=['Stock', 'Shares Owned', 'Last Price (USD)', 'USD Value'])
final_portfolio_df.to_csv(final_portfolio_filename, index=False)

# Print the final portfolio and total value
print(final_portfolio_df)
print(f"Total Portfolio Value (USD): {total_portfolio_value}")
print(f"Simulation complete. Final portfolio with last price and USD value saved to '{final_portfolio_filename}'")
