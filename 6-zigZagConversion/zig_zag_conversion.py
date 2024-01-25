"""
Difficulty: Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
"""

class Solution: #pylint: disable=too-few-public-methods
    """
    Solution class
    """
    def convert(self, s, num_rows):
        """
        First note that for the top and bottom rows,
        the indices increment by 2*num_rows-2. Then,
        for the middle rows, they split into two seperate
        increments. I.e for num_rows=5, the top and bottom rows
        increment by 2*5-2=8. Next, the second row increments by
        (6,2), the third by (4,4) and the fourth by (2,6).
        It will iterate over num_rows, so O(n), and for each row iterate over
        the length of the string, m, thus overall O(n*m)
        """
        if len(s) <=2 or num_rows==1:
            return s

        zig_zag = ""
        interval = [2*num_rows-2, 0]
        for r in range(num_rows):

            i = 0
            # Switch will alternate the interval
            switch = 0
            while r + i < len(s):
                switch %=2
                zig_zag += s[r+i]
                # If we use the zero increment, it will
                # double up
                if interval[1] == 0:
                    i+=interval[0]
                elif interval[0] == 0:
                    i+=interval[1]
                else:
                    i+=interval[switch]
                switch+=1
            # Update interval
            interval[0] -= 2
            interval[1] += 2
        return zig_zag
