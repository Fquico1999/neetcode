#!/usr/bin/env python3


"""
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
"""

from collections import deque

def is_valid(s:str)->bool:
    """
    This problem lends itself very well to a stack.
    In python, list operations to append items at the start or end is generally O(n),
    whereas if we use a deque instead, we can have pop/appends to start and end in O(1).

    First, we note that for s to be valid, it must have an even length.
    Something like ([) is obviously not valid.
    Next, we determine the center point, and we append each char in s to the deque
    until we reach the center point. After that we pop and compare to the next index in s.

    With this setup, since eache deque operation is O(1),
    overall we have O(n) time complexity, and O(3)+O(n) space complexity for the map and deque
    """

    if len(s) % 2 != 0:
        return False

    bracket_map = {'[':']',
                '(':')',
                '{': '}'} # This dict establishes which brackets are pairs

    stack = deque()

    for i, s_i in enumerate(s):
        if len(stack) > 0 and stack[-1] in bracket_map and s_i == bracket_map[stack[-1]]:
            stack.pop()
        else:
            stack.append(s[i])

    if len(stack) > 0:
        return False
    return True


if __name__ == "__main__":

    assert is_valid("()")
    assert not is_valid("{)}")
    assert is_valid("{{[(([]))]}}")
    assert not is_valid("[){}")
    assert is_valid('[]{}([])')
    assert not is_valid("([)]")
