"""
Difficulty: Medium
You are given a 0-indexed array of integers nums of length n.
You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1].
The test cases are generated such that you can reach nums[n - 1].
"""

class Solution:
    def jump(self, nums)->int:
        """
        Use a window / 2 ptr method where the window size is the jump distance.
        Within the window, find the index that would maximize the next window size.
        """
        if len(nums) <2:
            return 0
        num_jumps = 0
        l = 0           # left pointer
        r = l + nums[l] # right pointer

        while r < len(nums)-1:
            if nums[l] < 2:
                # Have to move to next index
                num_jumps+=1
                l+=1
                r = l+nums[l]
            else:
                # Check within the window for the index where a jump results in the largest index.

                i = l+1 # Start one after l
                best_r = i + nums[i] # Initialize the farthest r
                best_i = i
                # Search window for index that would give greatest r
                while i <= r:
                    if i + nums[i] >= best_r:
                        best_r = i+nums[i]
                        best_i = i
                    i+=1
                #After finding the best index, jump there
                num_jumps+=1
                l = best_i
                r = l + nums[l]
        return num_jumps+1




if __name__ == "__main__":
    test = Solution()

    n = [2,3,1,1,4]
    assert test.jump(n) == 2, "Expected 2"

    n = [2,3,0,1,4]
    assert test.jump(n) == 2, "Expected 2"

    n = [2,3,0,2,0,3,0,0,0]
    assert test.jump(n) == 4, "Expected 4"

    n = [10,9,8,7,6,5,4,3,2,1,1,0]
    assert test.jump(n) == 2, "Expected 2"
