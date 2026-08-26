

# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180.0, # Apple
    "GOOGL": 2700.0, # Google
    "MSFT": 330.0, # Microsoft
    "TSLA": 250.0, # Tesla
    "AMZN": 140.0 # Amazon
}

portfolio = {}

print("="*50)
print(" Welcome to Stock Portfolio Tracker")
print("="*50)

# Get stock and quantity from user
while True:
    stock_name = input("\nEnter stock symbol AAPL/GOOGL/MSFT/TSLA/AMZN or 'done': ").upper()
    
    if stock_name == 'DONE':
        break
    
    if stock_name not in stock_prices:
        print("Stock not found! Available:", list(stock_prices.keys()))
        continue
    
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity


# Calculate total investment
total_investment = 0
print("\n" + "="*50)
print(" YOUR PORTFOLIO SUMMARY")
print("="*50)
print(f"{'Stock':<10}{'Qty':<10}{'Price':<15}{'Value'}")
print("-"*50)

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_investment += value
    print(f"{stock:<10}{qty:<10}{price:<15}${value}")

print("-"*50)
print(f"Total Investment Value: ${total_investment:.2f}")
print("="*50)

# Save to txt file - optional
save = input("\nSave result to txt file? (yes/no): ").lower()
if save == 'yes':
    with open("portfolio_result.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("="*30 + "\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = qty * price
            f.write(f"{stock} - Qty: {qty}, Price: ${price}, Value: ${value}\n")
        f.write("="*30 + "\n")
        f.write(f"Total Investment Value: ${total_investment:.2f}\n")
    print("\nResult saved in 'portfolio_result.txt'")
