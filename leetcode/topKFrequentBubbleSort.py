"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]
"""
from collections import Counter
import heapq

class solutions:
    def topKFrequentBubbleSort(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        n = len(nums)
        buckets = [0] * (n + 1)
        
        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        print(buckets)

        res = []
        for i in range(n, 0, -1):
            if buckets[i] != 0:
                res.extend(buckets[i])
                if len(res) >= k:
                    break
        return res

s = solutions()
print(s.topKFrequentBubbleSort([1,1,1,2,2,3], 2))
print(s.topKFrequentBubbleSort([1,1,1,2,2,3,3,4], 2))
