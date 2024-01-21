"""
Test suite for insertDeleteGetRandomO(1)
"""

from insert_delete_get_random import RandomizedSet

def test1():
    """
    Test insertion
    """

    sol = RandomizedSet()
    assert sol.insert(4) is True, "Expected True"

def test2():
    """
    Test insertion of val already in set
    """
    sol = RandomizedSet()
    sol.insert(2)
    assert sol.insert(2) is False, "Expected False"

def test3():
    """
    Test removal of existing item.
    """
    sol = RandomizedSet()
    sol.insert(2)
    assert sol.remove(2) is True, "Expected True"

def test4():
    """
    Test removal of non-existing item.
    """
    sol = RandomizedSet()
    assert sol.remove(2) is False, "Expected False"

def test5():
    """
    Test get_random for one single item
    """
    sol = RandomizedSet()
    sol.insert(2)
    assert sol.get_random() == 2, "Expected 2"
