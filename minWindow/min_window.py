#!/usr/bin/env python3


"""
Difficulty: Hard

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that 
every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""

def min_window(s: str, t: str) -> str:
    """
    First implementation.
    """

    def is_subset(a: dict, b: dict)-> bool:
        # Check if a is contained in b
        for key in a.keys():
            if a[key] > b.get(key, 0):
                return False
        return True

    min_win = ""
    min_size = len(s)+1

    if len(t) > len(s):
        return min_win

    char_count = {}
    subchar_count = {}

    # Char count for t
    for i in enumerate(t):
        subchar_count[t[i]] = 1 + subchar_count.get(t[i], 0)


    l = 0

    for r, _ in enumerate(s):

        char_count[s[r]] = 1 + char_count.get(s[r], 0)

         # This operation is at worst O(52) (since its a-z, A-Z)
        print('pre',l,r,min_size,min_win,subchar_count,char_count)
        while l <= r and is_subset(subchar_count, char_count):
            if (r-l+1) < min_size:
                min_win = s[l:r+1]
                min_size = len(min_win)

                # If the size of the window is the same as len(t), can early stop
                if min_size == len(t):
                    return min_win

            #If the window is valid, then we'll decrease it by incrementing the left pointer
            char_count[s[l]] -=1

            l+=1

    return min_win

def min_window2(s:str, t:str)->str:
    """
    Better implementation
    """

    if len(t) > len(s):
        return ""

    # Store start and end indices of window
    min_win = [0,0]
    min_window_len = len(s)+1

    matches = 0

    window_char_count = {}
    target_char_count = {}
    for char in t:
        target_char_count[char] = 1 + target_char_count.get(char, 0)

    matches_needed = len(target_char_count.keys())

    l = 0
    for r,_ in enumerate(s):
        if s[r] in target_char_count:
            window_char_count[s[r]] = 1 + window_char_count.get(s[r], 0)

            if window_char_count[s[r]] == target_char_count[s[r]]:
                matches+=1


            while matches == matches_needed:
                if (r-l+1) < min_window_len:
                    min_win = [l,r+1]
                    min_window_len = r-l+1

                # Early stop if minWindowLen = len(t)
                if  min_window_len == len(t):
                    break


                if s[l] in target_char_count:
                    window_char_count[s[l]] -=1

                    if window_char_count[s[l]] < target_char_count[s[l]]:
                        matches-=1

                l+=1
    return s[min_win[0]:min_win[1]]



if __name__ == "__main__":

    S = "ADOBECODEBANCDOOOOOOOBANC"
    T = "AABC"
    OUT = "BANC"

    assert min_window2('abc', 'a') == 'a'
    assert min_window2('abcaabc', 'aa') == 'aa'
    assert min_window2('aa', 'aaa') == ''
    assert min_window2('adobecodebancdooo', 'abc') == 'banc'
