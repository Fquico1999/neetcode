"""
Difficulty: Medium

"""
import random

class RandomizedSet:
    """
    Implemntation of the RandomizedSet using an internal set and list.
    The list serves to allow random selection.
    """

    def __init__(self):
        self.randomized_set = set()
        self.items = []

    def insert(self, val)->bool:
        """
        Insert val into set. Set add/lookup is O(1)
        """
        if val in self.randomized_set:
            return False
        self.randomized_set.add(val)
        self.items.append(val)
        return True

    def remove(self, val)->bool:
        """
        Removes val from set using Python's remove() function.
        On average, O(1).
        """
        if val not in self.randomized_set:
            return False
        self.randomized_set.remove(val)
        self.items.remove(val)
        return True

    def get_random(self)->int:
        """
        Return random element using choice on items list
        """
        return random.choice(self.items)
