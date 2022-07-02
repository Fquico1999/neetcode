#!/usr/bin/env python3


"""
Difficulty: Hard

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that 
every character in t (including duplicates) is included in the window. 
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

def minWindow(s: str, t: str) -> str:

    def isSubset(a: dict, b: dict)-> bool:
        # Check if a is contained in b
        for key in a.keys():
            if a[key] > b.get(key, 0):
                return False
        return True

    minWindow = ""
    minSize = len(s)+1

    if len(t) > len(s):
        return minWindow

    charCount = {}
    subCharCount = {}

    # Char count for t
    for i in range(len(t)):
        subCharCount[t[i]] = 1 + subCharCount.get(t[i], 0)


    l = 0

    for r in range(len(s)):

        charCount[s[r]] = 1 + charCount.get(s[r], 0)

         # This operation is at worst O(52) (since its a-z, A-Z)
        print('pre',l,r,minSize,minWindow,subCharCount,charCount)
        while l <= r and isSubset(subCharCount, charCount):
            if (r-l+1) < minSize:
                minWindow = s[l:r+1]
                minSize = len(minWindow)

                # If the size of the window is the same as len(t), can early stop
                if minSize == len(t):
                    return minWindow

            #If the window is valid, then we'll decrease it by incrementing the left pointer
            charCount[s[l]] -=1

            l+=1

    return minWindow


if __name__ == "__main__":

    s = "ADOBECODEBANCDOOOOOOOBANC"
    t = "AABC"
    out = "BANC"

    print(minWindow('aa','aa'))