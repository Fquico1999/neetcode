#!/usr/bin/env python3

"""
Difficulty: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.""" 

"""


"""

def trap(height):
	"""
	Linear time. O(n) for creating maxLeft and maxRight and O(2n) space 
	"""

	trapSum = 0

	maxLeft = [0]*len(height)
	maxRight = [0]*len(height)

	for i in range(len(height)-1):
		j = len(height)-1-i

		if height[i] > maxLeft[i]:
			maxLeft[i+1] = height[i]
		else:
			maxLeft[i+1] = maxLeft[i]
	
		if height[j] > maxRight[j]:
			maxRight[j-1] = height[j]
		else:
			maxRight[j-1] = maxRight[j]

	for i in range(len(height)):
		trapSum += max(0, min(maxLeft[i], maxRight[i]) - height[i])
	return trapSum


if __name__ == "__main__":
	"""    _
       _   x_
     _ x_ _xx_
	_x_xx_xxxx
	   L     
		"""
	height = [0,1,0,2,1,0,1,3,2,1,2,1]
	ans = 6
	print(trap(height) == ans)