"""
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.
"""

def length_of_longest_substring(s):
    """
    2ptr implementation.
    """

    l, r = 0, 1
    max_length = 0

    while r <= len(s):
        if len(set(s[l:r])) == r-l:
            max_length = max(max_length, r-l)
        else:
            l+=1
        r+=1
    return max_length

def length_of_longest_substring2(s):
    """
    Second implementation using set.
    """
    l = 0
    max_length = 0
    char_set = set()

    for r,t in enumerate(s):
        while t in char_set:
            char_set.remove(s[l])
            l+=1
        char_set.add(t)
        max_length = max(max_length, r-l+1)
    return max_length


if __name__ == "__main__":
    S = "abcabcbb"
    ANS = 3
    print(length_of_longest_substring2(S))
