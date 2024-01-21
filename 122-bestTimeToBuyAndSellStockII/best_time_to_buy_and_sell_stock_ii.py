"""
Difficulty: Medium

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock.
You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
"""

class Solution:
    """
    Solution Class
    """
    def max_profit(self, prices)->int:
        """
        Implements O(n) time solution.
        The max profit is simply the sum of all positive deltas.
        """
        if len(prices) < 2:
            return 0
        max_profit = 0
        idx = 0
        while idx < len(prices)-1:
            if prices[idx] < prices[idx+1]:
                max_profit += prices[idx+1] - prices[idx]
            idx+=1
        return max_profit

if __name__ == "__main__":
    test = Solution()

    p = [7,1,5,3,6,4]
    assert test.max_profit(p) == 7, "Expected 7"
