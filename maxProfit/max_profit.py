
"""
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

"""

def max_profit_pointers(prices):
    """
    2 Pointer solution.
    """
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):

        if prices[r] < prices[l]:
            l = r
            r+=1
        else:

            profit = prices[r] - prices[l]

            if profit > max_profit:
                max_profit = profit
            r+=1
    return max_profit

if __name__ == "__main__":
    p = [7,1,5,3,6,4]
    print(max_profit_pointers(p))
