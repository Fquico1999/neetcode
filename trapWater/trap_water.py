#!/usr/bin/env python3

"""
Difficulty: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

def trap_arr(height):
    """
    Linear time. O(n) for creating max_left and max_right and O(2n) space
    """

    trap_sum = 0

    max_left = [0]*len(height)
    max_right = [0]*len(height)

    for i in range(len(height)-1):
        j = len(height)-1-i

        if height[i] > max_left[i]:
            max_left[i+1] = height[i]
        else:
            max_left[i+1] = max_left[i]

        if height[j] > max_right[j]:
            max_right[j-1] = height[j]
        else:
            max_right[j-1] = max_right[j]

    for i, h in enumerate(height):
        trap_sum += max(0, min(max_left[i], max_right[i]) - h)
    return trap_sum

def trap_lin(height):
    """
    Linear Time and constant space with two pointers.
    Recall that water is min(maxL, maxR) - height[i]
    """

    trap_sum = 0

    max_left, max_right = 0,0

    l,r = 0, len(height)-1

    while l < r:
        if height[l] > max_left:
            max_left = height[l]
        if height[r] > max_right:
            max_right = height[r]

        if max_left > max_right:
            # We know that max_right is smallest of the two, so
            trap_sum += max(max_right - height[r],0)
            r-=1
        else:
            trap_sum += max(max_left - height[l],0)
            l+=1
    return trap_sum


if __name__ == "__main__":
    # """    _
    #    _   x_
    #  _ x_ _xx_
    # _x_xx_xxxx
    #     L   R
    #     """
    h_arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    ANS = 6
    # print(trap(h) == ANS)
    print(trap_lin(h_arr))
