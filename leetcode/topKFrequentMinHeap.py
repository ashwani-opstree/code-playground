"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
"""
from collections import Counter
import heapq

class solutions:
    def topKFrequentHeap(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]

s = solutions()
print(s.topKFrequentHeap([1,1,1,2,2,3], 2))
