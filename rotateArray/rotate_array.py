"""
Difficulty: Medium

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    """
    Solution Class
    """
    def rotate(self, nums, k):
        """
        Use array slicing and swap slices, using tmp.
        """
        j = k % len(nums)
        tmp = nums[-j:]
        nums[j:] = nums[:-j]
        nums[:j] = tmp

    def rotate2(self, nums, k):
        """
        Array slicing in one line.
        """
        j = k % len(nums)
        nums[:] = nums[-j:] + nums[:-j]

    def rotate3(self, nums, k):
        """
        Move array elements by inserting and popping. Doesn't need additional memory.
        """
        for _ in range(k % len(nums)):
            nums.insert(0, nums.pop())

if __name__ == "__main__":
    test = Solution()

    n = [1,2,3,4,5,6,7]
    test.rotate3(n, 3)
    assert n == [5,6,7,1,2,3,4]

    n = [-1,-100,3,99]
    test.rotate3(n, 2)
    assert n == [3,99,-1,-100]

    n = [1]
    test.rotate3(n, 10)
    assert n == [1]

    n = [1,2,3,4]
    test.rotate3(n, 0)
    assert n == [1,2,3,4]

    n = [1,2]
    test.rotate3(n, 3)
    assert n == [2,1]
