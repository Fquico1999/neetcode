"""
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

class Solution(): #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def is_anagram(self, s, t)->bool:
        """
        Implementation of is_anagram using sorting. Sorting takes O(nlogn).
        sorted creates new list.
        """
        return sorted(s) == sorted(t)

    def is_anagram_hashmap(self, s, t)->bool:
        """
        Implementation using hashmap. O(n) to build each hashmap.
        """
        s_map, t_map = {},{}

        for c in s:
            if c in s_map:
                s_map[c]+=1
            else:
                s_map[c]=1
        for c in t:
            if c in t_map:
                t_map[c]+=1
            else:
                t_map[c]=1
        return s_map == t_map
