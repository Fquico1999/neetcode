"""
Difficulty: Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting
some (can be none) of the characters without disturbing the relative positions of the remaining
characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""

class Solution(): #pylint: disable=too-few-public-methods
    """
    Solution class
    """

    def is_subsequence(self, s, t):
        """
        Implementation using 2 pointers, one for the substring s and
        another for t. Essentially, we compare charaters in s to t,
        incrementing the s pointer when we find a match.
        We loop over t once, so it is O(len(t)).
        """
        if len(s) > len(t):
            return False
        if len(t) == 1:
            return s == t

        s_ptr = 0
        t_ptr = 0

        while t_ptr < len(t):
            # Check if we have matched all of s
            if s_ptr >= len(s):
                return True

            if s[s_ptr] == t[t_ptr]:
                s_ptr+=1

            t_ptr+=1

        if s_ptr >= len(s):
            return True
        return False
