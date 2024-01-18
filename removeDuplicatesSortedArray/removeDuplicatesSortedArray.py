"""
Difficulty: Easy

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1

        i = 1
        j = 1

        while (i < len(nums)):
            if nums[i] != nums[i-1]:
                #New unique
                nums[j] = nums[i]
                j+=1
            i+=1
        return j

if __name__ == "__main__":
    test = Solution()

    nums = [1,1,2]
    assert test.removeDuplicates(nums) == 2, "Expected 2"
    assert nums[:2] == [1,2], "Wrong"

    nums = [1,1,2,2,3,3]
    assert test.removeDuplicates(nums) == 3, "Expected 3"
    assert nums[:3] == [1,2,3], "Wrong"

    nums = [1]
    assert test.removeDuplicates(nums) == 1, "Expected 1"

    nums = [1,1,1,1,1,1,3]
    assert test.removeDuplicates(nums) == 2, "Expected 2"
    assert nums[:2] == [1,3], "Wrong"

    nums = [1,1,1,1,2,2,2,4]
    assert test.removeDuplicates(nums) == 3, "Expected 3"
    assert nums[:3] == [1,2,4], "Wrong"

    nums = [1,2]
    assert test.removeDuplicates(nums) == 2, "Expected 2"
    assert nums[:2] == [1,2], "Wrong"

    nums = [1,2,2]
    assert test.removeDuplicates(nums) == 2, "Expected 2"
    assert nums[:2] == [1,2], "Wrong"

    nums = [1,2,3]
    assert test.removeDuplicates(nums) == 3, "Expected 3"
    assert nums[:3] == [1,2,3], "Wrong"