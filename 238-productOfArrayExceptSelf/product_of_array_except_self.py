"""
Difficulty: Medium
Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution:
    """
    Solution Class
    """

    def product_except_self(self, nums):
        """
        Implementation using forward cumprod and reverse cumprod.
        """
        forward = [1]*len(nums)
        backward = [1]*len(nums)

        # Forward cumprod pass O(n)
        for i in range(1, len(nums)):
            forward[i] = nums[i-1]*forward[i-1]

        # Backward cumprod pass O(n)
        for i in range(len(nums)-2, -1, -1):
            backward[i] = nums[i+1]*backward[i+1]

        # List comprehension - O(n)
        array = [forward[i]*backward[i] for i in range(len(nums))]
        return array
