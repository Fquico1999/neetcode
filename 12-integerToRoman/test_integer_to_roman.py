"""
Test suite for integer to roman
"""

from integer_to_roman import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    num = 3
    assert sol.int_to_roman(num) == "III"

def test2():
    """
    Second leetcode test case
    """
    num = 58
    assert sol.int_to_roman(num) == "LVIII"

def test3():
    """
    Third leetcode test case
    """
    num = 1994
    assert sol.int_to_roman(num) == "MCMXCIV"
