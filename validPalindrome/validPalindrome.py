#!/usr/bin/env python3

"""
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

""" 
def isPalindrome(s: str) -> bool:
        
	# Filter out non alph characters based on ord
	s = ''.join([char for char in s.lower() if ((ord(char) >= ord('a') and ord(char) <= ord("z"))) or (ord(char) >= ord('0') and ord(char) <= ord('9'))])

	if len(s) <= 1:
		return True

	# Compare two pointers vs halving a list of chars and reversing. 
	for i in range(len(s)):
		j = len(s)-i-1

		if i >= j:
	    	return True
		if s[i] != s[j]:
	    	return False