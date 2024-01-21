#!/usr/bin/env python3

"""
Difficulty: Medium
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

1. Sort a Hashmap. Use a hashmap to store the frequency of each number in the input array.
Use sorted to sort based on the count.
Shound be around O(nlogn) time for the sorting and O(n) space for the HashMap.
Then we need to loop over k tuples to construct the output array. 
Space of output is O(k), so for k<n we have ~O(n) space.
Likewise, looping over k tuples is O(k), so we have ~O(nlogn) for this solution. 

"""

import heapq
from collections import defaultdict

def top_k_frequent_sort_hash(nums, k: int):
    """
    Implementation with sorting a hashmap
    """
    def sort_key(arr):
        """
        Function to sort array by second element
        """
        # want to sort by second element of tuple
        return arr[1]

    ret = []
    # Space complexity of O(n) with n being length of nums
    hashmap = defaultdict(int)
    # O(n) time complexity
    for elem in nums:
        hashmap[elem]+=1
    # Returns a list of tuples, should be O(nlogn)?
    sorted_by_counts = sorted(hashmap.items(), key=sort_key, reverse=True)
    # Loop over first k tuples and add first item to return array,  O (k)
    for (i,_) in sorted_by_counts[:k]:
        ret.append(i)
    # Overall should be O(nlogn+k)?
    return ret

def top_k_frequent_heap(nums, k: int):
    """
    Implementation using a heap.
    """
    # Create hashmap of occurences
    hashmap = {}
    heap = []
    #O(n) to count
    for num in nums:
        hashmap[num] = 1+hashmap.get(num, 0) # Alternative to using defaultdict
    # Want top k values. However, for tuples,
    # heap.pop will return smallest based on first element. So we must reverse the tuple
    # O(n) to loop
    for (num, count) in hashmap.items():
        # Want to add k elements into the heap
        if len(heap) < k:
            # O(logk) to push and pop
            heapq.heappush(heap, [count, num])
        else:
            heapq.heappushpop(heap, [count, num])
    # Final loop is O(k), so overall it seems like we have O(nlogk)
    return [num for (count, num) in heap]

def top_k_frequent_max_heap(nums, k: int):
    """
    heapq implementation is a min heap. Instead of O(nlogk), we can get O(klogn)
    by using a maxheap which we can obtain by inverting nums.
    This is because above we had a heap of size k and looped over n to populate and 
    pop elements since each poppush removed the min value.
    Here we are populating with n in linear time with heapify
    and popping k times.
    """

    # Create hashmap of occurences
    hashmap = {}
    ret = []
    #O(n) to count
    for num in nums:
        # Invert count to use maxheap
        hashmap[num] = -1+hashmap.get(num, 0) # Alternative to using defaultdict
    # Invert hashmap.items since heapq.heappop pops smallest tuple based on first index
    # This should be O(n) as well
    heap = [(count, num) for (num, count) in hashmap.items()]
    # heapify is O(n) and inplace
    heapq.heapify(heap)

    #O(k) with O(logn) pop, so overall O(klogn)
    for _ in range(k):
        (_, num) = heapq.heappop(heap)
        ret.append(num)

    # Overall we have O(3n + klogn) ~ O(klogn)
    return ret

def top_k_frequent_frequency_list(nums, k: int):
    """
    Implemenation using hashmap of occurences.
    """
    # Create hashmap of occurences
    hashmap = {}
    counts = [[] for _ in range(len(nums) + 1)]
    ret = []
    #O(n) to count
    for num in nums:
        hashmap[num] = 1+hashmap.get(num, 0) # Alternative to using defaultdict
    for (num, count) in hashmap.items():
        counts[count].append(num)

    # Start from end, and return top k values, skipping Nones.
    # outer loop is at most O(n)
    for i in range(len(counts)-1, 0, -1):
        if counts[i]:
            # Inner loop is at most O(n) HOWEVER this only occurs if all values are distinct
            #in which case it is O(n+n) since all other entries are None.
            for m in counts[i]:
                ret.append(m)
                if len(ret) == k:
                    return ret
    return []


if __name__=="__main__":
    n = [1,1,1,2,2,3]
    print(top_k_frequent_max_heap(n, 2))
