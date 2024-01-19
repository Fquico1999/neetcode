"""
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit.
Choose a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""

class Solution:
    def max_profit(self, prices)-> int:
        """
        Two pointer method to solve in linear time.
        Increment the right pointer untill a higher profit can be gained.
        Reset the left pointer when this occurs.
        """
        if len(prices) < 2:
            return 0

        max_profit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit > max_profit:
                max_profit=profit
            if prices[buy] > prices[sell]:
                buy = sell
                sell+=1
            else:
                sell+=1
        return max_profit

    def max_profit2(self, prices)->int:
        """
        Cleaner implementation of the solution.
        """
        if len(prices) < 2:
            return 0

        max_profit=0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            if price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit

if __name__ == "__main__":
    test = Solution()
    p = [7,1,5,3,6,4]
    assert test.maxProfit2(p) == 5, "Expected 5"

    p = [7,6,4,3,1]
    assert test.maxProfit2(p) == 0, "Expected 0"

    p = [7]
    assert test.maxProfit2(p) == 0, "Expected 0"

    p = [100,99,98,97,96,95,94,93,92,91,92]
    assert test.maxProfit2(p) == 1, "Expected 1"
