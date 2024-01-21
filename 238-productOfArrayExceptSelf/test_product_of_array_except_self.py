"""
Test Suite for product_of_array_except_self
"""
from product_of_array_except_self import Solution

sol = Solution()

def test1():
    """
    Monotonically increasing
    """
    n = [1,2,3,4]
    assert sol.product_except_self(n) == [24, 12, 8, 6], "Expected [24, 12, 8, 6]"

def test2():
    """
    Monotonically decreasing
    """
    n = [4,3,2,1]
    assert sol.product_except_self(n) == [6, 8, 12, 24], "Expected [6, 8, 12, 24]"

def test3():
    """
    Constant array
    """
    n = [2,2,2,2]
    assert sol.product_except_self(n) == [8, 8, 8, 8], "Expected [8,8,8,8]"

def test4():
    """
    Two element array
    """
    n = [2,1]
    assert sol.product_except_self(n) == [1,2], "Expected [1,2]"
