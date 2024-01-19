
"""
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def maxProfitPointers(prices):
    l, r = 0, 1
    maxProfit = 0
    while r < len(prices):

        if prices[r] < prices[l]:
            l = r
            r+=1
        else:

            profit = prices[r] - prices[l]

            if profit > maxProfit:
                maxProfit = profit
            r+=1
    return maxProfit





if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(maxProfitPointers(prices))
