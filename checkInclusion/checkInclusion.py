#!/usr/bin/env python3


"""
Difficulty: Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


def checkInclusion(s1: str, s2: str) -> bool:

	if len(s1) > len(s2):
		return False
	
	sub = sorted(s1) # Should be O(nlogn)

	l,r = 0, len(sub)-1

	while (r < len(s2)):

		if r-l+1 > len(sub):
			l+=1

		print(l,r,sorted(s2[l:r+1]), r-l+1,len(sub))
		if sorted(s2[l:r+1]) == sub:
			return True
		else:
			r+=1

	return False

def checkInclusionII(s1: str, s2:str)-> bool:
	"""
	The premise is that we use a sliding window of length s1 and repeatedly update the charCount of the sliding window
	untill it matches the charCount of s1.
	"""

	if len(s1) > len(s2):
		return False

	charCount = {}
	subCharCount = {}

	# Might as well make use of this loop to populate charCount, then we can start at len(s1) later

	# Keeping track of time complexities, let len(s1) = m, len(s2)=n
	# loop over m
	# Overall this is O(m*(1+1)) = 0(2m) ~ O(m)
	for i in range(len(s1)):
		# dict.get() is O(1)
		charCount[s2[i]] = 1 + charCount.get(s2[i],0)
		subCharCount[s1[i]] = 1+subCharCount.get(s1[i], 0)

	l = 0

	# Comparison here is at worst O(26). 
	if charCount.items() == subCharCount.items():
		return True

	# Loop is over n-m
	# Overall, at worst, O((n-m)(1+1+1+26)) = O(29(n-m))
	for r in range(len(s1), len(s2)):

		# Update the charCount of this window
		charCount[s2[r]] = 1 + charCount.get(s2[r], 0)
		charCount[s2[l]] -=1
		# Delete entry
		if charCount[s2[l]] == 0:
			charCount.pop(s2[l]) # O(1), not to be confused with list.pop which is only O(1) for the last element, otherwise it's O(n)
		l+=1

		# Comparison here is at worst O(26). 
		if charCount.items() == subCharCount.items():
			return True

	# Overall time complexity is ~O(n), but we can improve from ~O(26n) to O(26+n) by using a variable to track matches.
	return False




if __name__  == "__main__":

	s1 = "a"
	s2 = "ab"
	print(checkInclusionII(s1, s2))



