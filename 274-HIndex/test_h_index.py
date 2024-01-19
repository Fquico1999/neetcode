"""
Test Suite for H-Index solution.
"""
from h_index import Solution


sol = Solution()


def test1():
    """
    All ones
    """
    c = [1,1,1,1]
    assert sol.h_index(c) == 1, "Expecting 1"

def test2():
    """
    All fives
    """
    c = [5,5,5,5,5,5]
    assert sol.h_index(c) == 5, "Expected 5"