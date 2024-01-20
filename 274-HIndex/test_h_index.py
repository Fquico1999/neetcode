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

def test3():
    """
    There are two papers with 2 citations, thus we expect 2.
    """
    c = [1,2,2,3]
    assert sol.h_index(c) == 2, "Expected 2"

def test4():
    """
    There are more papers with 2 citations, however, there are
    at least 3 papers with 3, so we expect h index to be 3
    """
    c = [1,1,1,2,2,2,2,3,3,3]
    assert sol.h_index(c) == 3, "Expected 3"

def test5():
    """
    Array of non repeated integers, including 1.
    """
    c = [3,0,6,1,5]
    assert sol.h_index(c) == 3, "Expected 3"

def test6():
    """
    Array of non-repeated ints, excluding 1.
    """
    c = [2,4,3,5,3]
    assert sol.h_index(c) == 3, "Expected 3"

def test7():
    """
    Single value greater than zero
    """
    c = [100]
    assert sol.h_index(c) == 1, "Expected 1"

def test8():
    """
    Single zero.
    """
    c = [0]
    assert sol.h_index(c) == 0, "Expected 0"

def test9():
    """
    Multiple zeros.
    """

    c = [0,0,0]
    assert sol.h_index(c) == 0, "Expected 0"

def test10():
    """
    Large citations, small number of papers
    """

    c = [11,12]
    assert sol.h_index(c) == 2, "Expected 2"

def test11():
    """
    Smaller positive value last.
    """
    c = [0,3,2,0]
    assert sol.h_index(c) == 2, "Expected 2"
