#!/usr/bin/env python3


"""
Difficulty: Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


def checkInclusion(s1: str, s2: str) -> bool:
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

if __name__  == "__main__":

	s1 = "abc"
	s2 = "eidbaoocbao"
	print(checkInclusion(s1, s2))



