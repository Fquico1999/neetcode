"""
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution:
    def maxProfit(self, prices)-> int:
        if len(prices) < 2:
            return 0

        maxProfit = 0
        buy = 0
        sell = 1

        while (sell < len(prices)):
            profit = prices[sell] - prices[buy]
            if profit > maxProfit:
                maxProfit=profit
            if prices[buy] > prices[sell]:
                buy = sell
                sell+=1
            else:
                sell+=1
        return maxProfit

    def maxProfit2(self, prices)->int:
        if len(prices) < 2:
            return 0

        maxProfit=0
        minPrice = prices[0]
        for price in prices:
            if price < minPrice:
                minPrice = price
            if price - minPrice > maxProfit:
                maxProfit = price - minPrice
        return maxProfit

if __name__ == "__main__":
    test = Solution()
    prices = [7,1,5,3,6,4]
    assert test.maxProfit2(prices) == 5, "Expected 5"

    prices = [7,6,4,3,1]
    assert test.maxProfit2(prices) == 0, "Expected 0"

    prices = [7]
    assert test.maxProfit2(prices) == 0, "Expected 0"

    prices = [100,99,98,97,96,95,94,93,92,91,92]
    assert test.maxProfit2(prices) == 1, "Expected 1"
