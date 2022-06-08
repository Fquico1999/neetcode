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

import heapq
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

def topKFrequentHeap(nums: list[int], k: int) -> list[int]:
	# Create hashmap of occurences
	hashmap = {}
	heap = []
	#O(n) to count
	for num in nums:
		hashmap[num] = 1+hashmap.get(num, 0) # Alternative to using defaultdict
	# Want top k values. However, for tuples, heap.pop will return smallest based on first element. So we must reverse the tuple
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

def topKFrequentFrequencyList(nums: list[int], k: int) -> list[int]:
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
			for n in counts[i]:
				ret.append(n)
				if len(ret) == k:
					return ret 
					



if __name__=="__main__":
	nums = [1,1,1,2,2,3]
	k = 2
	print(topKFrequentFrequencyList(nums, k))
