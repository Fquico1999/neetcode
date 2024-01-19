#!/usr/bin/env python3

"""
Difficulty: Medium

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

A brute force solution would be O(n^2) time complexity, but we can do better.
We start with two pointers, left and right, at the ends of the array. Note that we can
"""

def maxArea(height):
    maxArea = 0
    l,r = 0, len(height)-1

    while (l < r):
        area = min(height[l], height[r])*(r-l)
        if area > maxArea:
            maxArea = area

        if height[l] > height[r]:
            r-=1
        else:
            l+=1
    return maxArea

if __name__ == "__main__":

    height = [10,10,11,1,1,1,1,1,1]

    print(maxArea(height))
