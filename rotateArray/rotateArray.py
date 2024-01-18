"""
Difficulty: Medium

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums, k):
        j = k % len(nums)
        tmp = nums[-j:]
        nums[j:] = nums[:-j]
        nums[:j] = tmp


if __name__ == "__main__":
    test = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    test.rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

    nums = [-1,-100,3,99]
    k = 2
    test.rotate(nums, k)
    assert nums == [3,99,-1,-100]

    nums = [1]
    k = 10
    test.rotate(nums, k)
    assert nums == [1]

    nums = [1,2,3,4]
    k = 0
    test.rotate(nums, k)
    assert nums == [1,2,3,4]

    nums = [1,2]
    k = 3
    test.rotate(nums, k)
    assert nums == [2,1]