#!/usr/bin/env python3

"""
Difficulty: Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

def dailyTemperaturesBrute(temperatures):

	ret = []

	for i in range(len(temperatures)):

		j = i 
		foundGreater = False
		while j < len(temperatures):
			if temperatures[j] > temperatures[i]:
				foundGreater = True 
				ret.append(j-i)
				break

			j+=1
		if not foundGreater:
			ret.append(0)
	return ret

def dailyTemperatures(temperatures):

	ret = [0]*len(temperatures)

	stack = []
	indices = []

	for i in range(len(temperatures)):

		while stack and temperatures[i] > stack[-1]:
			idx = indices.pop()
			elem = stack.pop()
			ret[idx] = i-idx
		stack.append(temperatures[i])
		indices.append(i)
	return ret


if __name__ == "__main__":

	assert dailyTemperaturesBrute([73,74,75,71,69,72,76,73]) ==  [1,1,4,2,1,1,0,0]

	assert dailyTemperaturesBrute([30,40,50,60]) ==  [1,1,1,0]

	assert dailyTemperatures([73,74,75,71,69,72,76,73]) ==  [1,1,4,2,1,1,0,0]

	assert dailyTemperatures([30,40,50,60]) ==  [1,1,1,0]

