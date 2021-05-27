'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Input = [7,1,5,3,6,4]
Output 5
'''

# Approach 1 - Brutal Force: 
# Basically, we just need to find the max value between 0 and profit 
# And find the minimum buy price to maximize the profit. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        maxi = 0
        minBuy = prices[0]
        for i in range(1, len(prices)):
            maxi = max(maxi, prices[i] - minBuy)
            minBuy = min(minBuy, prices[i])
        return maxi

# Approach 2 - DP
#    I want to use max between max, sell - buy 
#    if the sell is smaller than buy, we can just give it 0, by setting up max = 0
#    and we can set the sell = buy, to make the sell price smaller 
#
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        # We choose the max number first 
        smallest_sell = max(prices)
        maxi_profit = 0
        for price in prices:
            # When the current price is smaller than smallest, we assign it to be smallest, since we cannot make a profit. 
            # When the current price is bigger than smallest, it means that we can make a profit. 
            if price < smallest_sell:
                smallest_sell = price 
            maxi_profit = max(maxi_profit, price - smallest_sell)
        return maxi_profit

# Approach 3 - Greedy:
#     去找到最大的区间，我们先设置一个maxProfit，然后拿第一个数字作为minBuy，
#     如果当前这个数字低于最小购买，那么最小购买给它，
#     如果不是，那么他们的差就是当前的profit，拿它去和maxProfit比较，如果大于那么交换

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_buy_price = prices[0]
        max_profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] < min_buy_price:
                min_buy_price = prices[i]
            current_profit = prices[i] - min_buy_price
            if current_profit > max_profit:
                max_profit = current_profit
        return max_profit