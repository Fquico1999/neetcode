"""
Difficulty: Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

class Solution:
    """
    Solution Class
    """
    def majority_element(self, nums):
        """
        The solution loops through nums and creates a dict of num:count pairs. O(n) time, O(n) space
        Then it iterates through the dictionary and selects the num with the largest count.
        So overall, O(n) time and O(n) space.
        """
        if len(nums) == 1:
            return nums[0]

        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num] = 1
        m = nums[0]
        for num, count in d.items():
            if count > d[m]:
                m = num
        return m

    def majority_element_boyer_moore(self, nums):
        """
        Boyer-Moore Voting algorithm.
        Guarantees correctness if majority has more than n/2 occurances.
        O(n) time and O(1) space.
        """
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count +=1
            else:
                count -=1
        return candidate


if __name__ == "__main__":

    test = Solution()

    n = [1,2,2,2,1]
    assert test.majority_element(n) == 2, "Expected 2"
    assert test.majority_element_boyer_moore(n) == 2, "Expected 2"

    n = [0,1,2,3,3,3,3]
    assert test.majority_element(n) == 3, "Expected 3"
    assert test.majority_element_boyer_moore(n) == 3, "Expected 3"

    n = [1]
    assert test.majority_element(n) == 1, "Expected 1"
    assert test.majority_element_boyer_moore(n) == 1, "Expected 1"
