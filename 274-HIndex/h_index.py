"""
Difficulty: Medium

Given an array of integers citations where citations[i] is the number of citations
a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia:
The h-index is defined as the maximum value of h such that the given researcher has
published at least h papers that have each been cited at least h times.
"""

class Solution(): # pylint: disable=too-few-public-methods
    """
    Solution Class
    """
    def h_index(self, citations)-> int:
        """
        Implementation using python's sorted function.
        Sorting the array takes O(nlogn), and then iterating through
        takes at most O(n). So O(nlogn) time complexity.
        """
        citations.sort(reverse=True)
        h = 0
        for i, num in enumerate(citations):
            if num >= i+1:
                h = i+1
        return h
