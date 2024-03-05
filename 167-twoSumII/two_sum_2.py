"""
Difficulty: Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution.
You may not use the same element twice.
Your solution must use only constant extra space.
"""

class Solution(): #pylint: disable=too-few-public-methods
    """
    Solution class
    """

    def two_sum(self, numbers, target):
        """
        Implementation of Two sum II using 2 pointers.
        Right pointer instatiates to end of array.
        If the sum is larger, then decrement the right pointer.
        If the sum is smaller than target, increment the left.
        """
        # Guaranteed to be a solution
        if len(numbers) == 2:
            return [1,2]

        l = 0
        r = len(numbers)-1

        while l < len(numbers):
            ptr_sum = numbers[l] + numbers[r]

            if ptr_sum == target:
                return [l+1, r+1]

            if ptr_sum < target:
                l+=1
            else:
                r-=1

        return[-1,-1]
