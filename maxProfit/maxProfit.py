
"""
Difficulty: Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

def maxProfitBrute(prices):

	"""
	WOrks but is O(n^2) time complexity. 

	"""
	maxProfit = 0

	for i in range(len(prices)-1):
		buy = prices[i]

		for j in range(i+1, len(prices)):
			sell = prices[j]

			profit = sell - buy
			if profit > maxProfit:
				maxProfit = profit
	return maxProfit




if __name__ == "__main__":
	prices = [7,1,5,3,6,4]
	print(maxProfitBrute(prices))
