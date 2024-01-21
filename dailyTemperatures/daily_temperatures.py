#!/usr/bin/env python3

"""
Difficulty: Medium

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

def daily_temperatures_brute(temperatures):
    """
    Brute force solution.
    """

    ret = []

    for i, _ in enumerate(temperatures):

        j = i
        found_greater = False
        while j < len(temperatures):
            if temperatures[j] > temperatures[i]:
                found_greater = True
                ret.append(j-i)
                break

            j+=1
        if not found_greater:
            ret.append(0)
    return ret

def daily_temperatures(temperatures):
    """
    Stack implementation.
    """

    ret = [0]*len(temperatures)

    stack = []
    indices = []

    for i, _ in enumerate(temperatures):

        while stack and temperatures[i] > stack[-1]:
            idx = indices.pop()
            stack.pop()
            ret[idx] = i-idx
        stack.append(temperatures[i])
        indices.append(i)
    return ret


if __name__ == "__main__":

    assert daily_temperatures_brute([73,74,75,71,69,72,76,73]) ==  [1,1,4,2,1,1,0,0]

    assert daily_temperatures_brute([30,40,50,60]) ==  [1,1,1,0]

    assert daily_temperatures([73,74,75,71,69,72,76,73]) ==  [1,1,4,2,1,1,0,0]

    assert daily_temperatures([30,40,50,60]) ==  [1,1,1,0]
