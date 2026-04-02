# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr, If there are duplicates in arr, count then separately.

# arr = [1,2,3] (1+1), (1+2)
# output: 2

# arr = [1,1,3,3,5,5,7,7]
# output: 0

class solution:
	def countElements(self, arr: list[int]) -> int:
		s = set(arr)
		count = 0
		for x in arr:
			if x + 1 in s:
				count += 1
		return count

# print(solution().countElements([1,2,3]))
print(solution().countElements([3, 15, 7, 22, 9, 11, 5, 18, 27, 14, 6, 2, 30, 25, 19, 8, 12, 4, 21, 10]))