"""
Test suite for valid palindrome
"""

from valid_palindrome import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    s = "A man, a plan, a canal: Panama"
    assert sol.is_palindrome(s) is True

def test2():
    """
    Second leetcode test case
    """
    s = "race a car"
    assert sol.is_palindrome(s) is False

def test3():
    """
    Test case where s is a space
    """
    s = " "
    assert sol.is_palindrome(s) is True

def test4():
    """
    Test case where all characters are not alphanum
    """
    s = " .:. )(): "
    assert sol.is_palindrome(s) is True


def test5():
    """
    Test case where most characters are not alphanum
    """
    s = " .:..:asa:.  "
    assert sol.is_palindrome(s) is True

def test6():
    """
    Test with a single letter, one non alphanum
    """
    s = "a."
    assert sol.is_palindrome(s) is True
