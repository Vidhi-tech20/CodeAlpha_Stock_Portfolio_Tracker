# Hardcoded stock prices dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 310,
    "AMZN": 135
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", ", ".join(stock_prices.keys()))

# User input
while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not in list. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("⚠️ Please enter a valid number.")

# Calculate total investment
print("\n🧾 Investment Summary:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock}: {quantity} shares × ${price} = ${investment}")

print(f"\n💰 Total Investment: ${total_investment}")

# Optionally save to file
save = input("\nDo you want to save this report to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv extension): ")
    with open(filename, "w") as file:
        file.write("Stock,Quantity,Price,Investment\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            investment = price * quantity
            file.write(f"{stock},{quantity},{price},{investment}\n")
        file.write(f"\nTotal Investment,,,{total_investment}\n")
    print(f"📁 Report saved to {filename}")
