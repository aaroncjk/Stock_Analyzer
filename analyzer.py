# Calculate stock returns.
import math

# Initial investment: how much money is invested in the stock.
initial_investment = 10000

prices = [100, 110, 99]
prices.append(108)
prices.append(105)
# append adds an item to the end of a list.


def calculate_returns(prices):
    # if statement in handling invalid inputs, checking the list of prices is too short
    if len(prices) < 2:
        raise ValueError("At least two prices are required.")

    # making the prices in the list of prices are greater than zero
    # Price checking Loop using isinstance() to check whether a value belongs to a particular data type
    for price in prices:
        if not isinstance(price, (int, float)):
            raise ValueError("All prices must be numbers.")

        # rejecting infinity and NaN
        if not math.isfinite(price):
            raise ValueError("All prices must be finite.")

        if price <= 0:
            raise ValueError("All prices must be greater than zero.")

    returns = []

    for i in range(1, len(prices)):
        stock_return = (prices[i] - prices[i - 1]) / prices[i - 1]
        returns.append(stock_return)

    return returns


returns = calculate_returns(prices)

for stock_return in returns:
    print(f"Return (%): {stock_return * 100:.2f}")


def calculate_overall_returns(prices):
    returns = prices[-1] / prices[0] - 1
    return returns


overall_return = calculate_overall_returns(prices)


# Defining the final calculations
def calculate_final_value(prices, initial_investment):
    # validating initial investment similar to the prices in prices
    if not isinstance(initial_investment, (float, int)):
        raise ValueError("The initial investment must be a number.")

    if not math.isfinite(initial_investment):
        raise ValueError("Initial investment must be finite.")

    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")

    # Calculate final value and profit from the first observation to the last.
    final_value = initial_investment * (prices[-1] / prices[0])
    pnl = final_value - initial_investment

    return final_value, pnl


final_value, pnl = calculate_final_value(prices, initial_investment)

print(f"Returns (decimals): {returns}")
print(f"Overall Return (%): {overall_return * 100:.2f}")
print(f"Final Value: ${final_value:,.2f}")
print(f"PnL: ${pnl:,.2f}")
