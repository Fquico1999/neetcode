

"""
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


1. Sorting the string in python essentially splits into a char array and sorts alphabetically. If two words are anagrams they should have the same sorted char arrays.
Time complexity should be O(nlogn) due to the sorting. Space complexity is O(1).
"""
import unittest


def validAnagramSort(s: str, t: str) -> bool:
	if sorted(s) == sorted(t):
		return True 
	else:
		return False

def validAnagramHashMap(s: str, t: str) -> bool:
	if len(s)!= len(t):
		return False

	countS, countT = {},{}

	for i in range(len(s)):
		countS[s[i]] = 1+countS.get(s[i],0)
		countT[t[i]] = 1+countT.get(t[i],0)
	for c in countS:
		if countS[c] != countT.get(c,0):
			return False 
	return True

class Test(unittest.TestCase):
	def setUp(self):
		self.func = validAnagramSort

	def test_a(self):
		self.assertTrue(self.func("Hello", "elloH"))

	def test_b(self):
		self.assertFalse(self.func("Hello", "elloB"))

if __name__ == "__main__":
	unittest.main()