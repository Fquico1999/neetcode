

"""
Difficulty: Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.


1. Sorting the string in python essentially splits into a char array and sorts alphabetically.
If two words are anagrams they should have the same sorted char arrays.
Time complexity should be O(nlogn) due to the sorting. Space complexity is O(1).

2. HashMaps. So explicitly counting up occurences of each element and building up
HashMaps for s and t then comparing them. This should be O(s+t) for both time and space
"""
import unittest


def valid_anagram_sort(s: str, t: str) -> bool:
    """
    Implementation using Python's sorted()
    """
    return sorted(s) == sorted(t)

def valid_anagram_hash_map(s: str, t: str) -> bool:
    """
    Implementation using Hashmap
    """
    if len(s)!= len(t):
        return False

    count_s, count_t = {},{}

    for i, s_i in enumerate(s):
        count_s[s_i] = 1+count_s.get(s_i,0)
        count_t[t[i]] = 1+count_t.get(t[i],0)
    for c, val in count_s.items():
        if val != count_t.get(c,0):
            return False
    return True

class Test(unittest.TestCase):
    """
    Unittest Class
    """
    def setUp(self):
        self.func = valid_anagram_sort

    def test_a(self):
        """
        Test Hello with valid.
        """
        self.assertTrue(self.func("Hello", "elloH"))

    def test_b(self):
        """
        Test Hello with invalid.
        """
        self.assertFalse(self.func("Hello", "elloB"))

if __name__ == "__main__":
    unittest.main()
