"""
Difficulty: Medium

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place
such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution: # pylint: disable=too-few-public-methods
    """
    Solution Class
    """
    def remove_duplicates(self, nums):
        """
        Extend previous solution to allow for set number of repetitions.
        This is implemented by a counter to keep track of repeats.
        """
        if len(nums) < 2:
            return len(nums)

        num_unique = 2 # number of repetitions of unique allowed
        i = 1
        k = 1

        if nums[0] == nums[1]:
            c = 1
        else:
            c = 0
        while i < len(nums):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
                c=1
            else:
                if c < num_unique:
                    c+=1
                    nums[k] = nums[i]
                    k+=1

            i+=1

        return k



if __name__ == "__main__":
    test = Solution()

    n = [1,1,1,2,2]
    assert test.remove_duplicates(n) == 4, "Expected 4"
    assert n[:4] == [1,1,2,2]

    n = [1,1,1,2,2,2,3,3]
    assert test.remove_duplicates(n) == 6, "Expected 6"
    assert n[:6] == [1,1,2,2,3,3], "Wrong"

    n = [1,2,2,3,3,3,4]
    assert test.remove_duplicates(n) == 6, "Expected 6"
    assert n[:6] == [1,2,2,3,3,4], "Wrong"
