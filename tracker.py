# ================================
# Stock Portfolio Tracker
# ================================

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}
total_investment = 0

print("=" * 40)
print("      STOCK PORTFOLIO TRACKER")
print("=" * 40)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ${price}")

# Get number of stocks safely
while True:
    try:
        n = int(input("\nEnter the number of different stocks you own: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Input stock details
for i in range(n):
    print(f"\nStock {i + 1}")

    while True:
        stock_name = input("Enter Stock Symbol: ").strip().upper()

        if stock_name in stock_prices:
            break
        else:
            print("Stock not available! Please choose from the list above.")

    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid quantity! Please enter a whole number.")

    # If stock already exists, add the quantity
    if stock_name in portfolio:
        portfolio[stock_name] += quantity
    else:
        portfolio[stock_name] = quantity

# Display portfolio
print("\n" + "=" * 40)
print("        PORTFOLIO SUMMARY")
print("=" * 40)

for stock, quantity in portfolio.items():
    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"\nStock       : {stock}")
    print(f"Price       : ${stock_prices[stock]}")
    print(f"Quantity    : {quantity}")
    print(f"Investment  : ${investment}")

print("\n" + "=" * 40)
print(f"Total Investment Value = ${total_investment}")
print("=" * 40)

# Save report to text file
with open("portfolio_report.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")
    file.write("=" * 40 + "\n\n")

    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity

        file.write(f"Stock      : {stock}\n")
        file.write(f"Price      : ${stock_prices[stock]}\n")
        file.write(f"Quantity   : {quantity}\n")
        file.write(f"Investment : ${investment}\n")
        file.write("-" * 40 + "\n")

    file.write(f"\nTotal Investment Value = ${total_investment}\n")

print("\nPortfolio report has been saved as 'portfolio_report.txt'")