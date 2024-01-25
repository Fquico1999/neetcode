"""
Test suite for length of last word
"""

from length_of_last_word import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    s = "Hello World"
    assert sol.length_of_last_word(s) == 5

def test2():
    """
    Second leetcode test case
    """
    s = "   fly me   to   the moon  "
    assert sol.length_of_last_word(s) == 4
