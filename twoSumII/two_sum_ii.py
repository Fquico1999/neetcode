#!/usr/bin/env python3

"""
Difficulty: Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

1. Take two pointers. One at the start and one at the end. Since the numbers are ascending, we can compare the sum of right
and left pointer values to the target and increment/decrement the corresponding pointer. Worse case scenario is when
both numbers are central [1,2,3,4,5,6]. Even then its O(n) at worst. 

"""
def twoSum(numbers, target):#: List[int], target: int) -> List[int]:
    #Constant space means just the return array
    
    #Initalize  pointers
    i,j = 0,len(numbers)-1
    
    for _ in range(len(numbers)):
        test = numbers[i]+numbers[j]
        if test > target:
            j-=1
        elif test < target:
            i+=1
        else:
            return [i+1, j+1]

if __name__ == "__main__":
    print(twoSum([-1,0], -1))
