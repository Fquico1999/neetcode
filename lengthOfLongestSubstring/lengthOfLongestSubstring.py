#!/usr/bin/env python3


"""
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):

	l, r = 0, 1
	maxLength = 0

	while (r <= len(s)):
		if len(set(s[l:r])) == r-l:
			maxLength = max(maxLength, r-l)
		else:
			l+=1
		r+=1
	return maxLength



if __name__ == "__main__":
	s = "abcabcbb"
	s = " "
	ans = 3
	print(lengthOfLongestSubstring(s))