"""
Difficulty: Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place.
Ensure that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k:
- Change the array nums such that the first k elements of nums contain preserve their initial order.
  The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

class Solution:
    """
    Solution Class
    """
    def remove_duplicates(self, nums):
        """
        2 pointer implementation.
        One pointer loops through elements and the other tracks of where to insert unique elements.
        """
        if len(nums) == 1:
            return 1
        i = 1
        j = 1
        while i < len(nums):
            if nums[i] != nums[i-1]:
                #New unique
                nums[j] = nums[i]
                j+=1
            i+=1
        return j

if __name__ == "__main__":
    test = Solution()

    n = [1,1,2]
    assert test.remove_duplicates(n) == 2, "Expected 2"
    assert n[:2] == [1,2], "Wrong"

    n = [1,1,2,2,3,3]
    assert test.remove_duplicates(n) == 3, "Expected 3"
    assert n[:3] == [1,2,3], "Wrong"

    n = [1]
    assert test.remove_duplicates(n) == 1, "Expected 1"

    n = [1,1,1,1,1,1,3]
    assert test.remove_duplicates(n) == 2, "Expected 2"
    assert n[:2] == [1,3], "Wrong"

    n = [1,1,1,1,2,2,2,4]
    assert test.removeDuplicates(n) == 3, "Expected 3"
    assert n[:3] == [1,2,4], "Wrong"

    n = [1,2]
    assert test.removeDuplicates(n) == 2, "Expected 2"
    assert n[:2] == [1,2], "Wrong"

    n = [1,2,2]
    assert test.removeDuplicates(n) == 2, "Expected 2"
    assert n[:2] == [1,2], "Wrong"

    n = [1,2,3]
    assert test.removeDuplicates(n) == 3, "Expected 3"
    assert n[:3] == [1,2,3], "Wrong"
