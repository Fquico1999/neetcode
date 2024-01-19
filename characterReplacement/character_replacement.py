#!/usr/bin/env python3


"""
Difficulty: Medium

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


def characterReplacement(s: str, k: int) -> int:
    """
    Here we use a sliding window technique, which is O(n), and a hashmap to store letter frequencies
    Which needs to be iterated at most 26 times per loop, so O(26n) ~ O(n) time and O(26) space.
    """

    charCount = {}
    maxWindow = 0
    l = 0

    for r in range(len(s)):
        charCount[s[r]] = 1+charCount.get(s[r],0)

        while (r-l+1)-max(charCount.values()) > k:
            charCount[s[l]] -=1
            l+=1

        maxWindow = max(maxWindow, (r-l+1))

    return maxWindow

def characterReplacementII(s, k):

    l = 0
    maxFreq = 0
    charCount = {}
    maxWindow = 0

    for r in range(len(s)):
        charCount[s[r]] = 1+charCount.get(s[r],0)

        maxFreq = max(maxFreq, charCount[s[r]])

        # Check if it's a valid substring, if not, increment the left pointer
        while (r-l+1) - maxFreq > k:
            charCount[s[l]]-=1
            l+=1
        maxWindow = max(maxWindow, r-l+1)

    return maxWindow

if __name__ == "__main__":
    S="ABAA"
    K=1
    ANS = 4
    print(characterReplacementII(S,K))
