#!/usr/bin/env python3

"""
Difficulty: Medium
Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

"""

def longest_consecutive(nums):# List[int]) -> int:
    longest = 0
    # O(n) space
    nums = set(nums)

    # O(n)
    for num in nums:

        if num-1 not in nums:
            # Found a starting point
            print(num)
            length = 1
            a = num
            # At most this will run n times.
            #If it runs n times, it means that the outer for loop only runs once, so still 0(n)
            while a+1 in nums:
                length+=1
                a +=1
            if length > longest:
                longest = length
    return longest




if __name__ == "__main__":
    n = [0,3,7,2,5,8,4,6,0,1,100]
    print(longest_consecutive(n))
