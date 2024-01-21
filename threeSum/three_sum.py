#!/usr/bin/env python3

"""
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

def three_sum_brute(nums):
    """
    Implementation using sorted.
    """
    # Sort in O(nlogn)
    nums = sorted(nums)
    ret = set()

    # i iterates n times, j iterates n-1 times, k iterates n-2 times, so O(n^3)

    for i, num in enumerate(nums):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):

                if num + nums[j] + nums[k] == 0 and (num, nums[j], nums[k]) not in ret:
                    ret.add((num, nums[j], nums[k]))

    return ret

def three_sum(nums):
    """
    More efficient implementation.
    """
    nums = sorted(nums)
    ret = []
    # visited = set()

    for i,a in enumerate(nums):
        if a>0:
            break
        if i>0 and a==nums[i-1]:
            continue

        j,k = i+1, len(nums)-1
        while j<k:
            t_sum = a + nums[j] + nums[k]


            if t_sum < 0 :
                j+=1
            elif t_sum > 0:
                k-=1
            else:
                ret.append([a, nums[j], nums[k]])
                j+=1
                while nums[j] == nums[j-1] and j<k:
                    j+=1
    return ret


if __name__ == "__main__":
    n = [-1,0,1,2,-1,-4]
    print(three_sum(n))
