"""
Test suite for zig zag conversion
"""

from zig_zag_conversion import Solution

sol = Solution()

def test1():
    """
    First test case from leetcode
    """
    s = "PAYPALISHIRING"
    num_rows = 3
    assert sol.convert(s, num_rows) == "PAHNAPLSIIGYIR"

def test2():
    """
    Second leetcode test case
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    """
    s = "PAYPALISHIRING"
    num_rows = 4
    assert sol.convert(s, num_rows) == "PINALSIGYAHRPI"


def test3():
    """
    Third leetcode test case
    """
    s = "A"
    num_rows = 1
    assert sol.convert(s, num_rows) == "A"

def test4():
    """
    Three letter case
    """
    s = "PAL"
    num_rows = 2
    assert sol.convert(s, num_rows) == "PLA"

def test5():
    """
    PAYPALISHIRING with 5 rows
    """
    s = "PAYPALISHIRING"
    num_rows = 5
    assert sol.convert(s, num_rows) == "PHASIYIRPLIGAN"

def test6():
    """
    One row test case
    """
    s = "ABC"
    num_rows=1
    assert sol.convert(s, num_rows) == "ABC"
