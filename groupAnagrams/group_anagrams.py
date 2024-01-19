#!/usr/bin/env python3

"""
Difficulty: Medium
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

1. Sorting. If we sort the words in the list, then two words are anagrams if their sorted list is identical.
If sorting is O(nlogn) where n is the mean length of input string but we must do this m times,
where m is the number of strings so overall, O(mnlogn)

2. Occurance counting. Since it goes from a-z we have 26 letters,
so instead we can count up each occurence of the letters for each of the input strings
Counting the letters loops over the string length, let's say on average it is n,
and we need to do so for all strings, m. so we have O(mn) which is better
than the sorting method. Technocally we count over all words, so its O(26mn) ~ O(mn)
"""

from collections import defaultdict


def group_anagrams_sort(strs):# list[str]) -> list[list[str]]:
    """
    Solution using sorted method. O(mnlogn) time complexity.
    """
    # First we need to create a hashmap from sorted word to word
    hashmap = {}
    for elem in strs:
        elem_sorted = ''.join(sorted(elem))
        if elem_sorted in hashmap:
            hashmap[elem_sorted].append(elem)
        else:
            hashmap[elem_sorted] = [elem]

    # Now the problem is done. We just need to return the values
    return list(hashmap.values())

def group_anagrams_count(strs):# list[str]) -> list[list[str]]:
    """
    Occurence counting solution using enumeration of lower case alpha chars.
    """
    hashmap = {}
    # O(m) for m strings in strs
    for elem in strs:
        count = 0
        # Here we loop over 26
        for i,letter in enumerate(list('abcdefghijklmnopqrstuvwxyz')):
            # Counting is O(n)
            count+=elem.count(letter)*10**i
        if count in hashmap:
            hashmap[count].append(elem)
        else:
            hashmap[count] = [elem]
    return list(hashmap.values())

def group_anagrams_count_better(strs):
    """
    Occurence counting using ord() function.
    """
    # set default to list so we don't have to create it if it doesnt exist
    hashmap = defaultdict(list)

    # O(m) for m strings in strs
    for elem in strs:

        # Space complexity is O(26) for this list
        count = [0]*26
        # Here we only have to loop over chars in elem so O(n) for n average length of elem
        for char in elem:
            count[ord(char) - ord('a')] +=1

        # list is unhashable, so convert to tuple
        hashmap[tuple(count)].append(elem)
    return list(hashmap.values())


if __name__ == "__main__":

    s = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams_count(s))
