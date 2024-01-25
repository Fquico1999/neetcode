"""
Test suite for is_anagram
"""

from valid_anagram import Solution

# Create solution object that can be used by all the tests
sol = Solution()

def test1():
    """
    First test from leetcode.
    """
    s ="anagram"
    t = "nagaram"
    assert sol.is_anagram(s, t) is True
    assert sol.is_anagram_hashmap(s, t) is True

def test2():
    """
    Second test case from leetcode
    """
    s = "rat"
    t = "car"
    assert sol.is_anagram(s,t) is False
    assert sol.is_anagram_hashmap(s,t) is False
