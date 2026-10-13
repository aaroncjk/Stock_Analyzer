# Calculate stock returns.

# Initial investment: how much money is invested in the stock.
initial_investment = 10000

prices = [100, 110, 99]
prices.append(108)
prices.append(105)
# append adds an item to the end of a list.

returns = []
#range sets a position to each price
for i in range(1, len(prices)):
    stock_return = (prices[i] - prices[i - 1]) / prices[i - 1]
    returns.append(stock_return)
    print(f"Return (%): {stock_return * 100:.2f}")

overall_return = prices[-1] / prices[0] - 1

# Calculate final value and profit from the first observation to the last.
final_value = initial_investment * (prices[-1] / prices[0])
profit = final_value - initial_investment


print(f"Returns (decimals): {returns}")
print(f"Overall Return (%): {overall_return * 100:.2f}")
print(f"Final Value: ${final_value:,.2f}")
print(f"Profit: ${profit:,.2f}")
