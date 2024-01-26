"""
Difficulty: Easy

Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.
"""

class Solution: #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def str_str(self, haystack, needle)->int:
        """
        Implementation using try except block surrounding built in 
        .index method. This is on average O(n)
        """
        try:
            i = haystack.index(needle)
        except ValueError:
            i = -1
        return i

    def str_str2(self, haystack, needle)->int:
        """
        Implementation using pointer. time complexity is O(n)
        """
        i = 0
        while i < len(haystack):
            # Needle counter
            c = 0
            while c < len(needle) and haystack[i+c] == needle[c]:
                c+=1
            if c == len(needle):
                return i
            # If it fails immediately, we need to increment by 1
            i +=max(1, c)
        return -1
