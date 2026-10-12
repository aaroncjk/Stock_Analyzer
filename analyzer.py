#calculating the returns on stocks 

#Initial investment, How much money i put into this stock 
initial_investment = 10000

prices = [100,110,99]
prices.append(108)
#append means adding an element to the end of a list 

first_returns = ((prices[1] - prices[0])/ prices[0]) * 100
second_returns = ((prices[2] - prices[1])/ prices[1]) *100
third_returns = ((prices[3] - prices[2])/ prices[2]) *100
overall_returns = ((prices[-1] - prices[0])/ prices[0]) * 100

#Computing the final value and the profit from the first year to the final year 
final_value = initial_investment * (prices[-1]/prices[0])
profit = final_value - initial_investment


print(f"First Return(%): {first_returns:.2f}")
print(f"Second Return(%): {second_returns:.2f}")
print(f"Third Return(%): {third_returns:.2f}")
print(f"Overall Return(%): {overall_returns:,.2f}")
print(f"Final Value: ${final_value:,.2f}")
print(f"Profit: ${profit:,.2f}")
