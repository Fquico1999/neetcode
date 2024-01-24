"""
Test suite for roman to integer
"""

from roman_to_integer import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    s = "III"
    assert sol.roman_to_int(s) == 3
    assert sol.roman_to_int2(s) == 3

def test2():
    """
    Test Exceptions
    """
    s = "IV"
    assert sol.roman_to_int(s) == 4
    assert sol.roman_to_int2(s) == 4

def test3():
    """
    Test Exceptions
    """
    s = "IX"
    assert sol.roman_to_int(s) == 9
    assert sol.roman_to_int2(s) == 9

def test4():
    """
    Test Exceptions
    """
    s = "XL"
    assert sol.roman_to_int(s) == 40
    assert sol.roman_to_int2(s) == 40

def test5():
    """
    Test Exceptions
    """
    s = "CM"
    assert sol.roman_to_int(s) == 900
    assert sol.roman_to_int2(s) == 900
