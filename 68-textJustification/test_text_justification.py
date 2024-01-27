"""
Test suite for text justification
"""

from text_justification import Solution

sol = Solution()

def test1():
    """
    First leetcode test case
    """
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    max_width = 16
    assert sol.full_justify(words, max_width) == ["This    is    an",
                                                  "example  of text", 
                                                  "justification.  "]

def test2():
    """
    Second leetcode test case
    """
    words = ["What","must","be","acknowledgment","shall","be"]
    max_width = 16
    assert sol.full_justify(words, max_width) == ["What   must   be",
                                                  "acknowledgment  ", 
                                                  "shall be        "]

def test3():
    """
    Third leetcode test case
    """
    words = ["Science","is","what","we","understand","well", "enough","to","explain", 
             "to","a","computer.","Art","is","everything","else","we","do"]
    max_width = 20
    assert sol.full_justify(words, max_width) == ["Science  is  what we",
                                                  "understand      well", 
                                                  "enough to explain to", 
                                                  "a  computer.  Art is", 
                                                  "everything  else  we", 
                                                  "do                  "]
