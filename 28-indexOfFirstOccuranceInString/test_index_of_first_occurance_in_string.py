"""
Test suite for index of first occurance in string
"""

from index_of_first_occurance_in_string import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    haystack = "sadbutsad"
    needle = "sad"
    assert sol.str_str(haystack, needle) == 0
    assert sol.str_str2(haystack, needle) == 0

def test2():
    """
    Second leetcode test case
    """
    haystack = "leetcode"
    needle = "leeto"
    assert sol.str_str(haystack, needle) == -1
    assert sol.str_str2(haystack, needle) == -1

def test3():
    """
    Test case where complete match is at end
    """
    haystack = "leetleetleetleeto"
    needle="leeto"
    assert sol.str_str(haystack, needle) == 12
    assert sol.str_str2(haystack, needle) == 12

def test4():
    """
    Test case with single matching letter
    """
    haystack = "l"
    needle="l"
    assert sol.str_str(haystack, needle) == 0
    assert sol.str_str2(haystack, needle) == 0

def test5():
    """
    Test case with single mismatching letter
    """
    haystack = "l"
    needle="e"
    assert sol.str_str(haystack, needle) == -1
    assert sol.str_str2(haystack, needle) == -1
