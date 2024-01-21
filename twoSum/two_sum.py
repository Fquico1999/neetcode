#!/usr/bin/env python3

"""
Difficulty: Easy
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

1. Brute Force solution is O(n^2) time complexity.

2. Hash Map: create a hash map of array where key is array value and value is the index.
We want to check if the difference between the current element and the
target exists in the hash map. Time Complexity is O(n) since worst case we need to loop
once over the array. The space complexity is O(n) for the HashMap
"""

def two_sum_brute(nums, target: int):
    """
    Brute force implementation O(n^2)
    """
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] + nums[j] == target:
                return [i,j]
    return [0,0]

def two_sum_hash(nums, target: int):
    """
    Hashmap implementation in O(n)
    """
    hashmap = {elem:i for i, elem in enumerate(nums)}
    for i,elem in enumerate(nums):
        if target-elem in hashmap and i != hashmap[target-elem]:
            return [i, hashmap[target-elem]]
    return [0,0]


if __name__ == "__main__":
    print(two_sum_hash([2,15,11,7], 9))
