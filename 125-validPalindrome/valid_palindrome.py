"""
Difficulty: Easy
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution(): #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def is_palindrome(self, s):
        """
        Implementation using 2Ptrs. O(n) time complexity since the word
        is only traversed once.
        """

        s = s.lower()
        l = 0
        r = len(s)-1

        while l <= r:
            while not s[l].isalnum() and l < r:
                l+=1

            while not s[r].isalnum() and l < r:
                r-=1

            if s[l] != s[r]:
                return False

            l+=1
            r-=1

        return True
