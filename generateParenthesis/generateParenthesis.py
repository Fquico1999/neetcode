#!/usr/bin/env python3

"""
Difficulty: Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

def generateParenthesis( n: int):
	res_arr = []

	def recursion(n, stack, ret):

		if (n==0):
			while stack:
				ret += ')'
				stack.pop()
			res_arr.append(ret)
			return True
		#print(stack)
		recursion(n-1, stack + ["("], ret + '(') # push

		if stack:
			stack.pop()
			recursion(n, stack, ret + ')')

	recursion(n, [], "")
	return res_arr


if __name__ == "__main__":
	print(generateParenthesis(3))

