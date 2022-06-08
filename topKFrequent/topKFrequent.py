#!/usr/bin/env python3

"""
Difficulty: Medium
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

"""
1. Sort a Hashmap. Use a hashmap to store the frequency of each number in the input array. Use sorted to sort based on the count.
Shound be around O(nlogn) time for the sorting and O(n) space for the HashMap. Then we need to loop over k tuples to construct the output array. 
Space of output is O(k), so for k<n we have ~O(n) space. Likewise, looping over k tuples is O(k), so we have ~O(nlogn) for this solution. 
"""

import matplotlib.pyplot as plt
import numpy as np
import time
from collections import defaultdict

def topKFrequentSortHash(nums: list[int], k: int) -> list[int]:
        def sortKey(arr):
        	# want to sort by second element of tuple
       		return arr[1]
        
        ret = []
        # Space complexity of O(n) with n being length of nums
        hashmap = defaultdict(int)
        # O(n) time complexity
        for elem in nums:
                hashmap[elem]+=1
        # Returns a list of tuples, should be O(nlogn)?
        sorted_by_counts = sorted(hashmap.items(), key=sortKey, reverse=True)
        # Loop over first k tuples and add first item to return array,  O (k)
        for (k,v) in sorted_by_counts[:k]:
            ret.append(k)
        # Overall should be O(nlogn+k)?
        return ret
