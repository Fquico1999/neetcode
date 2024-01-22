"""
Test suite for trapping Rain water
"""

from trapping_rain_water import Solution

sol = Solution()

def test1():
    """
    First leetcode example
    """
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert sol.trap(height) == 6

def test2():
    """
    Second leetcode example
    """
    height = [4,2,0,3,2,5]
    assert sol.trap(height) == 9
