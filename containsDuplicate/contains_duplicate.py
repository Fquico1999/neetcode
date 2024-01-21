"""
Difficulty: Easy
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

1. Brute force solution is O(n^2) time-complexity but O(1) space.

2. Sorting array first groups duplicates, allowing us to only loop over the array once.
Checking for duplicates is O(n) time complexity, but with sorting, it becomes O(nlogn).
Don't need extra space if we discount space required for sorting, so O(1)

3. HashSet. Check if item exists in HashSet then add it. 
Checking takes O(1) for n items, so O(n) time complexity.
Space complexity is O(n) for the HashSet
"""
# import unittest
# import big_o


# @profile
def contains_duplicates_brute(nums)->bool:
    """
    Brute force solution.
    """
    for n in nums:
        for m in nums:
            if n==m:
                return True
    return False

# @profile
def contains_duplicates_sort(nums)->bool:
    """
    Solution using Python's sorted().
    """
	# Python's sorted() is Timsort
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

# @profile
def contains_duplicates_hash(nums)->bool:
    """
    Hashset solution.
    """
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

# class TestBrute(unittest.TestCase):
#     """
#     Class to implement unit tests.
#     """

#     def test_simple_true(self):
#         self.assertTrue(contains_duplicates_brute([1,2,1,4]))


#     def test_simple_false(self):
#         self.assertFalse(contains_duplicates_brute([1,2,3,4]))


#     def test_small_true(self):
#         self.assertTrue(contains_duplicates_brute([1,1]))


#     def test_small_false(self):
#         self.assertTrue(contains_duplicates_brute([1,2]))

#     def test_large_true_1(self):
#         self.assertTrue(contains_duplicates_brute([1,9,2,0,4,3,2,1,1]))


#     def test_large_true_2(self):
#         self.assertTrue(contains_duplicates_brute([1,9,2,0,4,3,2,2,2]))

# class TestSort(unittest.TestCase):

#     def test_simple_true(self):
#         self.assertTrue(contains_duplicates_brute([1,2,1,4]))

#     def test_simple_false(self):
#         self.assertFalse(contains_duplicates_brute([1,2,3,4]))

#     def test_small_true(self):
#         self.assertTrue(contains_duplicates_brute([1,1]))

#     def test_small_false(self):
#         self.assertTrue(contains_duplicates_brute([1,2]))

#     def test_large_true_1(self):
#         self.assertTrue(contains_duplicates_brute([1,9,2,0,4,3,2,1,1]))

#     def test_large_true_2(self):
#         self.assertTrue(contains_duplicates_brute([1,9,2,0,4,3,2,2,2]))

if __name__ == "__main__":
	# Profile Memory usage on simple example
    t = [1,2,3,5,1]
    contains_duplicates_brute(t)
    contains_duplicates_sort(t)
    contains_duplicates_hash(t)

	# positive_int_generator = lambda n: big_o.datagen.integers(n, 0, 10000)
	# best_brute, others = big_o.big_o(containsDuplicatesBrute, positive_int_generator, n_repeats=1000)
	# # best_sort, others = big_o.big_o(containsDuplicatesSort, positive_int_generator, n_repeats=100)

	# print("Brute Force:\n")
	# print(best_brute)


	# print("Sorting First\n")
	# print(best_sort)
