"""
Test suite for reverse words in a string
"""

from reverse_words_in_a_string import Solution

sol = Solution()

def test1():
    """
    First test case from leetcode
    """
    s = "the sky is blue"
    assert sol.reverse_words(s) == "blue is sky the"

def test2():
    """
    Second test case from leetcode
    """
    s = "  hello world  "
    assert sol.reverse_words(s) == "world hello"
