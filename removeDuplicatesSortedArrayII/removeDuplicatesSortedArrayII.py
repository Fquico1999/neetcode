"""
Difficulty: Medium

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)

        num_unique = 2 # number of repetitions of unique allowed
        i = 1
        j = 1

        if nums[0] == nums[1]:
            c = 1
        else:
            c = 0
        while(i < len(nums)):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j+=1
                c=1
            else:
                if c < num_unique:
                    c+=1
                    nums[j] = nums[i]
                    j+=1
            i+=1
        return j



if __name__ == "__main__":
    test = Solution()

    nums = [1,1,1,2,2]
    assert test.removeDuplicates(nums) == 4, "Expected 4"
    assert nums[:4] == [1,1,2,2]

    nums = [1,1,1,2,2,2,3,3]
    assert test.removeDuplicates(nums) == 6, "Expected 6"
    assert nums[:6] == [1,1,2,2,3,3], "Wrong"

    nums = [1,2,2,3,3,3,4]
    assert test.removeDuplicates(nums) == 6, "Expected 6"
    assert nums[:6] == [1,2,2,3,3,4], "Wrong"