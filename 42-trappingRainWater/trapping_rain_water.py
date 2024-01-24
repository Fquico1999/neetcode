"""
Difficulty: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

class Solution: #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def trap(self, height)->int:
        """
        O(n) implementation using two extra arrays. These contain the max
        height seen from left-to-right and right-to-left respectively.
        O(n) per iteration over height, so O(3n)~O(n) and O(2n) in space.
        """
        # If there is only one height, return zero
        if len(height) < 2:
            return 0

        trap_sum = 0

        # These will contain the max height seen from left to right
        # and right to left.
        max_l_arr = [height[0]]*len(height)
        max_r_arr = [height[-1]]*len(height)

        for i in range(1, len(height)):
            max_l_arr[i] = max(max_l_arr[i-1], height[i])

        for i in range(len(height)-2, -1, -1):
            max_r_arr[i] = max(max_r_arr[i+1], height[i])

        for i, h in enumerate(height):
            trap_sum += max(min(max_l_arr[i], max_r_arr[i]) - h, 0)

        return trap_sum
