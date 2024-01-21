"""
Difficulty: Easy

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, 
you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
- The remaining elements of nums are not important as well as the size of nums.
- Return k.
"""

class Solution:
    """
    Solution Class
    """
    def removeElementOld(self, nums, val):

        i = len(nums)-1 # pointer 1
        j = i # pointer 2
        k = 0 # Keep track of how many swaps
        while (i >= 0):
            if nums[i] == val:
                k+=1
                i-=1
                j-=1
            else:
                while (nums[j] != val and j >= 0):
                    j-=1
                # Either got to the end, or found val
                if j < 0:
                    return len(nums) - k
                elif nums[j] == val:
                    #swap
                    nums[j] = nums[i]
                    nums[i] = val
                    k+=1
                    i-=1
        # reached the end
        return len(nums) - k

    def removeElement(self, nums, val):
        # While this is much cleaner, the old algorithm is roughly twice as fast because it minimizes
        # the number of swaps.
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
        return i



if __name__ == "__main__":
    test = Solution()

    n = [0,1,2,2,3,0,4,2]
    assert test.removeElement(n, 2) == 5, "Expected 5"
    assert n[-3:] == [2,2,2], "Wrong"

    n = [3,2,2,3]
    assert test.removeElement(n, 2) == 2, "Expected 2"
    assert n[-2:] == [2,2], "Wrong"

    n = [0,1,2,2,3,0,4,2]
    assert test.removeElement(n, 2) == 5, "Expected 5"
    assert n[-3:] == [2,2,2], "Wrong"
