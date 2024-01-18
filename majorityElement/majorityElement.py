"""
Difficulty: Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums):
        """
        The solution loops through nums and creates a dict of num:count pairs. O(n) time, O(n) space
        Then it iterates through the dictionary and selects the num with the largest count, also O(n)
        So overall, O(n) time and O(n) space.
        """
        if len(nums) == 1:
            return nums[0]

        d = {}
        for num in nums:
            if num in d.keys():
                d[num]+=1
            else:
                d[num] = 1
        max = nums[0]
        for num, count in d.items():
            if count > d[max]:
                max = num
        return max


if __name__ == "__main__":

    test = Solution()

    nums = [1,2,2,2,1]
    assert test.majorityElement(nums) == 2, "Expected 2"

    nums = [0,1,2,3,3,3,3]
    assert test.majorityElement(nums) == 3, "Expected 3"

    nums = [1]
    assert test.majorityElement(nums) == 1, "Expected 1"