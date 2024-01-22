"""
Test suite for Candy problem.
"""
from candy import Solution

sol = Solution()

def test1():
    """
    Intial leetcode example
    """
    ratings = [1,0,2]
    assert sol.candy(ratings) == 5

def test2():
    """
    Second leetcode test
    """
    ratings = [1,2,2]
    assert sol.candy(ratings) == 4

def test3():
    """
    Case where there are two minima
    """
    ratings = [1,0,2,1,2]
    assert sol.candy(ratings) == 8

def test4():
    """
    Single child
    """
    ratings = [1]
    assert sol.candy(ratings) == 1

def test5():
    """
    Equal ratings
    """
    ratings = [2,2,2,2,2]
    assert sol.candy(ratings) == 5

def test6():
    """
    Monotonic increase
    """
    ratings = [1,2,3,4]
    assert sol.candy(ratings) == 10

def test7():
    """
    Monotonic decrease
    """
    ratings = [4,3,2,1]
    assert sol.candy(ratings) == 10

def test8():
    """
    Increase followed by plateau and then decrease
    """
    ratings = [1,2,3,4,4,3,2,1]
    assert sol.candy(ratings) == 20

def test9():
    """
    
    """
    ratings = [1,3,4,5,2]
    assert sol.candy(ratings) == 11
