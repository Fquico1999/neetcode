"""
Difficulty: Easy
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

class Solution: #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def length_of_last_word(self, s)->int:
        """
        Implementation using built in string methods.
        """
        return len(s.strip().split()[-1])
