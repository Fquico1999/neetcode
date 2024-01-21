#!/usr/bin/env python3


"""
Difficulty: Medium

You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same
letter you can get after performing the above operations.
"""


def character_replacement(s: str, k: int) -> int:
    """
    Here we use a sliding window technique, which is O(n), and a hashmap to store letter frequencies
    Which needs to be iterated at most 26 times per loop, so O(26n) ~ O(n) time and O(26) space.
    """

    char_count = {}
    max_window = 0
    l = 0

    for r, _ in enumerate(s):
        char_count[s[r]] = 1+char_count.get(s[r],0)

        while (r-l+1)-max(char_count.values()) > k:
            char_count[s[l]] -=1
            l+=1

        max_window = max(max_window, (r-l+1))

    return max_window

def character_replacement2(s, k):
    """
    2Ptr alternative implementation.
    """

    l = 0
    max_freq = 0
    char_count = {}
    max_window = 0

    for r, _ in enumerate(s):
        char_count[s[r]] = 1+char_count.get(s[r],0)

        max_freq = max(max_freq, char_count[s[r]])

        # Check if it's a valid substring, if not, increment the left pointer
        while (r-l+1) - max_freq > k:
            char_count[s[l]]-=1
            l+=1
        max_window = max(max_window, r-l+1)

    return max_window

if __name__ == "__main__":
    S="ABAA"
    K=1
    ANS = 4
    print(character_replacement2(S,K))
