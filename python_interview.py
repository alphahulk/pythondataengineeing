# Python Interview Questions. (Asked in Volkswagen Group from hashtag#AWS data engineer role)

# 1. You are given a list of stock prices, where the stock's price on the i-th day is stored as the i-th element of the prices list.
# You want to maximize your profit trading the stock, but are only allowed to buy the stock once and sell it once on a future day.
# Write a function called max_profit which takes in this list of stock prices and computes the maximum profit possible. Return 0 if you can't make any profit.
# Input: prices = [9, 1, 3, 6, 4, 8, 3, 5, 5] Output: 7 Explanation: Buy on day 2 (price = 1) and sell on day 6 (price = 8), profit = 8 - 1 = 7.

prices = [9, 1, 3, 6, 4, 8, 3, 5, 5]
def max_price(prices):
    max_price=0
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            current_prof=prices[j]-prices[i]
            print(current_prof)
    if current_prof > max_profit:
        max_profit = current_prof
        return max_profit
    print(max_profit)


