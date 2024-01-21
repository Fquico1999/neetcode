"""
Difficulty: Medium

You are given an integer array nums.
You are initially positioned at the array's first index.
Each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    """
    Solution Class
    """
    def can_jump(self, nums)->bool:
        """
        O(n) solution. Observation is that each entry adds to the greatest "Reach".
        """
        if len(nums) < 2:
            return True

        can_reach_index = nums[0]
        i = 0
        while i <= can_reach_index:
            can_reach_index = max(can_reach_index, i + nums[i])
            if can_reach_index >= len(nums)-1:
                return True
            i+=1
        return False


if __name__ == "__main__":
    test = Solution()
    n = [1,2,5,1,0,0,0]
    assert test.can_jump(n) is True, "Expected True"

    n = [0]
    assert test.can_jump(n) is True, "Expected True"

    n = [1,1,1,1,0,0]
    assert test.can_jump(n) is False, "Expected False"

    n = [1,4,2,1,9,0,0,0,0,0]
    assert test.can_jump(n) is True, "Expected True"
