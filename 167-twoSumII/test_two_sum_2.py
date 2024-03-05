"""
Test suite for Two Sum II
"""

from two_sum_2 import Solution

sol = Solution()

def test1():
    """
    First neetcode test case
    """
    numbers = [2,7,11,15]
    target = 9
    assert sol.two_sum(numbers, target) == [1,2], "Expected [1,2]"

def test2():
    """
    Second neetcode test case
    """
    numbers = [2,3,4]
    target = 6
    assert sol.two_sum(numbers, target) == [1,3], "Expected [1,3]"

def test3():
    """
    Third neetcode test case
    """
    numbers = [-1,0]
    target = -1
    assert sol.two_sum(numbers, target) == [1,2], "Expected [1,2]"

def test4():
    """
    indices are middle
    """
    numbers = [2, 3, 4, 6]
    target = 7
    assert sol.two_sum(numbers, target) == [2,3], "Expected [2,3]"

def test5():
    """
    Solution is last indices
    """
    numbers = [0,1,2,3,4,5]
    target = 9
    assert sol.two_sum(numbers, target) == [5,6], "Expected [5,6]"

def test6():
    """
    Solution is staggered last
    """
    numbers = [1,2,4,5,6]
    target = 10
    assert sol.two_sum(numbers, target) == [3,5], "Expected [3,5]"


def test7():
    """
    Case where greedy increment of right pointer fails.
    """
    numbers = [1,4,5,7,10]
    target = 9
    assert sol.two_sum(numbers, target) == [2,3], "Expected [2,3]"

def test8():
    "Case where sum is zero"

    numbers = [0,0,3,4,5]
    target = 0
    assert sol.two_sum(numbers, target) == [1,2], "Expected [1,2]"

def test9():
    """
    Case with negative numbers
    """
    numbers = [-3,3,4,90]
    target = 0
    assert sol.two_sum(numbers, target) == [1,2], "Expected [1,2]"

def test10():
    """
    Long example
    """
    numbers = [12,13,23,28,43,44,59,60,61,68,
               70,86,88,92,124,125,136,168,173,
               173,180,199,212,221,227,230,277,
               282,306,314,316,321,325,328,336,
               337,363,365,368,370,370,371,375,
               384,387,394,400,404,414,422,422,
               427,430,435,457,493,506,527,531,
               538,541,546,568,583]
    target = 542
    assert sol.two_sum(numbers, target) == [24, 32], "Expected [24,32]"
