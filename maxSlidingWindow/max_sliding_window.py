#!/usr/bin/env python3
"""
Difficulty: Hard

You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.
"""

import collections

def max_sliding_window(nums, k):
    """
    Siliding window implementation.
    """

    if k > len(nums):
        return []

    max_val = -float("infinity")

    l = 0

    # Find maxval in first k nums
    for r in range(k):
        max_val = max(max_val, nums[r])

    max_window = [max_val]

    for r in range(k, len(nums)):

        max_val = max(max_val, nums[r])

        if nums[l] == max_val:
            max_val = -float("infinity")
            # Need to refind maxVal within window
            for num in nums[l+1:r+1]:
                max_val = max(max_val, num)

        max_window.append(max_val)
        l+=1
    return max_window


def max_sliding_window_deque(nums, k):
    """
    A deque - double ended queue - is a data structure
    that has fast appends/pops from either end - O(1)
    With thus data structure, we can iterate over nums
    and ensure that only the largest element seen so far is in the deque
    """
    output = []
    # Store indices so we can compare the left pointer
    # directly to the left of the deque in O(1) time.
    window = collections.deque()

    l = r = 0

    while r < len(nums):
        # Before we append nums[r], we need to ensure that every element in the deque
        # Must be larger
        while window and nums[window[-1]] < nums[r]:
            window.pop() #O(1)

        window.append(r) # O(1)
        #At this point we can be certain that the first element of the deque is the largest

        #Now we need to ensure that the left index is not out of bounds
        if l > window[0]:
            window.popleft()

        #Ensure window is at least size k before adding to output
        if (r+1)>= k:
            output.append(nums[window[0]])
            l+=1
        r+=1
    return output

if __name__ == "__main__":

    assert max_sliding_window_deque([1,3,-1,-3,5,3,6,7], 3) ==  [3,3,5,5,6,7]
    assert max_sliding_window_deque([1,1,1,1], 2) ==  [1,1,1]
    assert max_sliding_window_deque([5,4,3,2,1], 3) ==  [5,4,3]
    assert max_sliding_window_deque([6,4,3,4,6], 1) == [6,4,3,4,6]
