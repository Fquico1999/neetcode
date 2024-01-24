"""
Difficulty: Easy

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution: # pylint: disable=too-few-public-methods
    """
    Solution class
    """

    def roman_to_int(self, s) -> int:
        """
        Implementation using dict to store conversion between symbol and number. Additionally, 
        the six exceptions are checked explicitly. Fixed size dict, so O(1) space, and O(n) time.
        """

        sym_to_val = {"I":1,
                      "V":5,
                      "X":10,
                      "L":50,
                      "C":100,
                      "D":500,
                      "M":1000}

        # Assign first char
        roman = sym_to_val[s[0]]

        # For the exceptions, we retroactively subtract the value of the prefix.
        for i in range(1, len(s)):
            if s[i] == "V" and s[i-1] == "I":
                roman+= 4-1
            elif s[i] == "X" and s[i-1] == "I":
                roman+= 9-1
            elif s[i] == "L" and s[i-1] == "X":
                roman+= 40-10
            elif s[i] == "C" and s[i-1] == "X":
                roman+= 90-10
            elif s[i] == "D" and s[i-1] == "C":
                roman+= 400-100
            elif s[i] == "M" and s[i-1] == "C":
                roman+= 900-100
            else:
                roman += sym_to_val[s[i]]

        return roman

    def roman_to_int2(self, s) -> int:
        """
        Implementation using dict to store conversion between symbol and number. However, instead of
        explicitly checking the exceptions, we observe that every time they occur, they are followed
        by a larger value.
        """

        sym_to_val = {"I":1,
                      "V":5,
                      "X":10,
                      "L":50,
                      "C":100,
                      "D":500,
                      "M":1000}

        # Assign first char
        roman = sym_to_val[s[0]]

        # For the exceptions, we retroactively subtract the value of the prefix.
        for i in range(1, len(s)):
            if sym_to_val[s[i]] > sym_to_val[s[i-1]]:
                roman += sym_to_val[s[i]] - 2*sym_to_val[s[i-1]]
            else:
                roman += sym_to_val[s[i]]

        return roman
