#!/usr/bin/env python3

"""
Difficulty: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

"""

def is_palindrome(s: str) -> bool:
    """
    Using pointers.
    """

    # Filter out non alph characters based on ord
    s = ''.join([char for char in s.lower() if ((ord(char) >= ord('a') and ord(char) <= ord("z")))
                 or (ord(char) >= ord('0') and ord(char) <= ord('9'))])

    if len(s) <= 1:
        return True

    # Compare two pointers vs halving a list of chars and reversing.
    for i,s_i in enumerate(s):
        j = len(s)-i-1

        if i >= j:
            return True
        if s_i != s[j]:
            return False
    return False


def is_palindrome_list(s: str) -> bool:
    """
    Using list.
    """

    # Filter out non alph characters based on ord
    s = ''.join([char for char in s.lower() if ((ord(char) >= ord('a') and ord(char) <= ord("z")))
                 or (ord(char) >= ord('0') and ord(char) <= ord('9'))])

    return list(s) == list(s)[::-1]

if __name__ == "__main__":

    ST = "A man, a plan, a canal: Panama"
    print(is_palindrome(ST))
    print(is_palindrome_list(ST))
