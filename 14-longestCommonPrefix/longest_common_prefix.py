"""
Difficulty: Easy
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

class Solution: #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def longest_common_prefix(self, strs) -> str:
        """
        Implementation that iterates over the first string's characters and
        checks if the others have it as well. If l is the average length of 
        a word, and n is the number of words, then this runs in O(l*n)
        Vertical Scanning approach.
        """

        prefix = ""
        for i, c in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != c:
                    return prefix

            prefix +=c
        return prefix
