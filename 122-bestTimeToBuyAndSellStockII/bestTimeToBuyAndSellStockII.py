"""
Difficulty: Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""

class Solution:
    def maxProfit(self, prices)->int:
        if len(prices) < 2:
            return 0
        maxProfit = 0
        idx = 0
        while (idx < len(prices)-1):
            if prices[idx] < prices[idx+1]:
                maxProfit += prices[idx+1] - prices[idx]
            idx+=1
        return maxProfit

if __name__ == "__main__":
    test = Solution()

    prices = [7,1,5,3,6,4]
    assert test.maxProfit(prices) == 7, "Expected 7"