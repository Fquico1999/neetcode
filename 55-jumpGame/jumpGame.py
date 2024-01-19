"""
Difficulty: Medium

You are given an integer array nums.
You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums)->bool:
        """
        O(n) solution. Observation is that each entry adds to the greatest "Reach".
        """
        if len(nums) < 2:
            return True

        canReachIndex = nums[0]
        i = 0
        while (i <= canReachIndex):
            canReachIndex = max(canReachIndex, i + nums[i])
            if canReachIndex >= len(nums)-1:
                return True
            i+=1
        return False


if __name__ == "__main__":
    test = Solution()
    nums = [1,2,5,1,0,0,0]
    assert test.canJump(nums) == True, "Expected True"

    nums = [0]
    assert test.canJump(nums) == True, "Expected True"

    nums = [1,1,1,1,0,0]
    assert test.canJump(nums) == False, "Expected False"

    nums = [1,4,2,1,9,0,0,0,0,0]
    assert test.canJump(nums) == True, "Expected True"