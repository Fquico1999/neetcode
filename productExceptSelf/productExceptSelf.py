#!/usr/bin/env python3

"""
Difficulty: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

"""
1. Prefix cumprod and postfix cumprod. Both take O(n), and done sequentially, we get two O(2n) ~ O(n), and we need O(n) space complexity for it
since we construct a pre, post and output array. 

2. If we use the output array to construct our pre and post fixes, we can get O(1) space since the output array space complexity doesnt count.
What we do in the first pass is for i, we compute the prefix prod (arr[0]*arr[1]...*arr[i-1]) and store it in out[i].
For the second pass we compute the postfix and multiply the prefix at i. 

"""

def productExceptSelf(nums):# list[int]) -> list[int]:
    """
    [2,3,1,3]
    [3*1*3, 2*1*3, 2*3*3, 2*3*1]
    [2, 5, 6, 9]
    """

    # Can do better than copy which is likely O(n)
    prefix = nums.copy()
    postfix = nums.copy()
    output = [0]*len(nums)
    # Compute pre and post fix
    for i in range(len(nums) -1):
        prefix[i+1] = prefix[i]*nums[i+1]
        postfix[len(nums)-i-2] = postfix[len(nums)-i-1]*nums[len(nums)-i-2]
    # So now, the prod except self is just the prod of prefix[i-1]*postfix[i+1]
    for i in range(len(nums)):
        if i-1 < 0:
            output[i]=1
        else:
            output[i] = prefix[i-1]

        if i+1 > len(nums)-1:
            output[i]*=1
        else:
            output[i]*=postfix[i+1]
    return output

def productExceptSelfTwoPass(nums): #list[int]) -> list[int]:
    output = [0]*len(nums)

    # Prefix Pass
    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix*=nums[i]
    print(output)
    
    #Postfix pass
    postfix=1
    for i in range(len(nums)-1,-1, -1):
        print(i,postfix)
        output[i]*=postfix
        postfix*=nums[i]
    print(output)


if __name__ == "__main__":
    print(productExceptSelfTwoPass([1,2,3,4]))
