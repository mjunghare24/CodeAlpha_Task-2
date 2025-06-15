# tracker.py

from stock_prices import STOCK_PRICES
import os

def get_user_portfolio():
    portfolio = {}
    print("Enter your stock holdings. Type 'done' when finished.")
    while True:
        stock = input("Stock symbol (e.g., AAPL): ").upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("Stock not found in price list. Try again.")
            continue
        try:
            quantity = int(input(f"Quantity of {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Invalid quantity. Try again.")
    return portfolio

def calculate_total_investment(portfolio):
    total = 0
    for stock, quantity in portfolio.items():
        total += STOCK_PRICES[stock] * quantity
    return total

def save_to_file(portfolio, total, filetype="txt"):
    os.makedirs("output", exist_ok=True)
    filename = f"output/portfolio_summary.{filetype}"
    with open(filename, "w") as f:
        if filetype == "csv":
            f.write("Stock,Quantity,Price,Total Value\n")
            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * quantity
                f.write(f"{stock},{quantity},{price},{value}\n")
            f.write(f"\nTotal Investment,,,{total}\n")
        else:
            f.write("Your Portfolio Summary:\n\n")
            for stock, quantity in portfolio.items():
                price = STOCK_PRICES[stock]
                value = price * quantity
                f.write(f"{stock}: {quantity} x ${price} = ${value}\n")
            f.write(f"\nTotal Investment: ${total}\n")
    print(f"Portfolio saved to {filename}")

def main():
    portfolio = get_user_portfolio()
    if not portfolio:
        print("No stocks entered.")
        return

    total = calculate_total_investment(portfolio)
    print(f"\nTotal Investment Value: ${total}")

    save = input("Save portfolio to file? (y/n): ").lower()
    if save == 'y':
        filetype = input("File type (txt/csv): ").lower()
        if filetype not in ['txt', 'csv']:
            filetype = 'txt'
        save_to_file(portfolio, total, filetype)

if __name__ == "__main__":
    main()
