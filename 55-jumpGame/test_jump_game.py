"""
Test suite for jumpGame
"""
from jump_game import Solution

sol = Solution()

def test1():
    n = [1,2,5,1,0,0,0]
    assert sol.can_jump(n) is True, "Expected True"

def test2():
    n = [0]
    assert sol.can_jump(n) is True, "Expected True"

def test3():
    n = [1,1,1,1,0,0]
    assert sol.can_jump(n) is False, "Expected False"

def test4():
    n = [1,4,2,1,9,0,0,0,0,0]
    assert sol.can_jump(n) is True, "Expected True"
