#!/usr/bin/env python3


"""
Difficulty: Hard

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
"""
def maxSlidingWindow(nums, k):

    if k > len(nums):
        return []

    maxVal = -float("infinity")
    
    l = 0

    # Find maxval in first k nums
    for r in range(k):
        maxVal = max(maxVal, nums[r])

    maxWindow = [maxVal]

    for r in range(k, len(nums)):

        maxVal = max(maxVal, nums[r])

        if nums[l] == maxVal:
            maxVal = -float("infinity")
            # Need to refind maxVal within window
            for num in nums[l+1:r+1]:
                maxVal = max(maxVal, num)

        maxWindow.append(maxVal)
        l+=1
    return maxWindow



if __name__ == "__main__":

    assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) ==  [3,3,5,5,6,7]
    assert maxSlidingWindow([1,1,1,1], 2) ==  [1,1,1]
    assert maxSlidingWindow([5,4,3,2,1], 3) ==  [5,4,3], "Expected %s but instead got %s" % ([5,4,3], maxSlidingWindow([5,4,3,2,1], 3))
    assert maxSlidingWindow([6,4,3,4,6], 1) == [6,4,3,4,6]
