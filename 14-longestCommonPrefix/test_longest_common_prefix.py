"""
Test suite for longest common prefix
"""

from longest_common_prefix import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    strs = ["flower","flow","flight"]
    assert sol.longest_common_prefix(strs) == "fl"

def test2():
    """
    Second leetcode test case.
    """
    strs = ["dog","racecar","car"]
    assert sol.longest_common_prefix(strs) == ""

def test3():
    """
    All words are the same
    """
    strs = ["hello", "hello", "hello"]
    assert sol.longest_common_prefix(strs) == "hello"

def test4():
    """
    Shorter words after the first
    """
    strs = ["ab", "a"]
    assert sol.longest_common_prefix(strs) == "a"
