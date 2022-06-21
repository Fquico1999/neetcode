#!/usr/bin/env python3

"""
Difficulty: Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
 and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""     

def threeSumBrute(nums):
    # Sort in O(nlogn)
    nums = sorted(nums)
    ret = set()

    # i iterates n times, j iterates n-1 times, k iterates n-2 times, so O(n^3)

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):

                if nums[i] + nums[j] + nums[k] == 0 and (nums[i], nums[j], nums[k]) not in ret:
                    ret.add((nums[i], nums[j], nums[k]))

    return ret

def threeSum(nums):
    nums = sorted(nums)
    ret = []
    visited = set()

    for i,a in enumerate(nums):
        if a>0:
            break
        if i>0 and a==nums[i-1]:
            continue

        j,k = i+1, len(nums)-1
        while(j<k):
            threeSum = a + nums[j] + nums[k]


            if threeSum < 0 :
                j+=1
            elif threeSum > 0:
                k-=1
            else:
                ret.append([a, nums[j], nums[k]])
                j+=1
                while nums[j] == nums[j-1] and j<k:
                    j+=1
    return ret

        

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))