"""
Test suite for gasStation
"""
from gas_station import Solution

sol = Solution()

def test1():
    """
    First example from leetcode.
    """
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    assert sol.can_complete_circuit_brute(gas, cost) == 3
    assert sol.can_complete_circuit_window(gas, cost) == 3
    assert sol.can_complete_circuit_optimized(gas, cost) == 3

def test2():
    """
    No solution.
    """
    gas = [2,3,4]
    cost = [3,4,3]
    assert sol.can_complete_circuit_brute(gas, cost) == -1
    assert sol.can_complete_circuit_window(gas, cost) == -1
    assert sol.can_complete_circuit_optimized(gas, cost) == -1

def test3():
    """
    Case where solution is last index
    """
    gas = [1,1,3,0,5]
    cost = [2,2,1,3,1]
    assert sol.can_complete_circuit_brute(gas, cost) == 4
    assert sol.can_complete_circuit_window(gas, cost) == 4
    assert sol.can_complete_circuit_optimized(gas, cost) == 4

def test4():
    """
    No solution. Tests a condition where right increments past max
    in the window implementation.
    """
    gas = [4,5,2,6,5,3]
    cost = [3,2,7,3,2,9]
    assert sol.can_complete_circuit_window(gas, cost) == -1
    assert sol.can_complete_circuit_optimized(gas, cost) == -1


def test5():
    """
    Example without solution.
    """
    gas = [1,2,3,4,3,2,4,1,5,3,2,4]
    cost = [1,1,1,3,2,4,3,6,7,4,3,1]
    assert sol.can_complete_circuit_window(gas, cost) == -1
    assert sol.can_complete_circuit_optimized(gas, cost) == -1

def test6():
    """
    Small arrays that check the looparound.
    """
    gas = [3,1,1]
    cost = [1,2,2]
    assert sol.can_complete_circuit_window(gas, cost) == 0
    assert sol.can_complete_circuit_brute(gas, cost) == 0
    assert sol.can_complete_circuit_optimized(gas, cost) == 0
