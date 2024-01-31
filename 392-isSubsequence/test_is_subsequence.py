"""
Test suite for isSubsequence
"""

from is_subsequence import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    s = "abc"
    t = "ahbgdc"
    assert sol.is_subsequence(s, t) is True

def test2():
    """
    Second leetcode test case
    """
    s = "axc"
    t = "ahbgdc"
    assert sol.is_subsequence(s, t) is False
