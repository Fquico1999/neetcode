#!/usr/bin/env python3

"""
Difficulty: Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""

"""
1. Sorting. If we sort the words in the list, then two words are anagrams if their sorted list is identical.
If sorting is O(nlogn) we need to sort n times
"""

def groupAnagramsSort(strs: list[str]) -> list[list[str]]:

	# First we need to create a hashmap from sorted word to word
	hashmap = {}
	for elem in strs:
		elem_sorted = ''.join(sorted(elem))
		if elem_sorted in hashmap:
			hashmap[elem_sorted].append(elem)
		else:
			hashmap[elem_sorted] = [elem]

	# Now the problem is done. We just need to return the values
	return list(hashmap.values())



if __name__ == "__main__":

	strs = ["eat","tea","tan","ate","nat","bat"]
	print(groupAnagramsSort(strs))