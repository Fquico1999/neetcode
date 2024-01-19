"""
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):

    l, r = 0, 1
    maxLength = 0

    while (r <= len(s)):
        if len(set(s[l:r])) == r-l:
            maxLength = max(maxLength, r-l)
        else:
            l+=1
        r+=1
    return maxLength

def lengthOfLongestSubstring2(s):
    l = 0
    maxLength = 0
    charSet = set()

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        maxLength = max(maxLength, r-l+1)
    return maxLength


if __name__ == "__main__":
    S = "abcabcbb"
    ANS = 3
    print(lengthOfLongestSubstring2(S))
