# Given an interger array, return true if any value appears at least twice in the array, and return false if every element is distinct.

class solution:
	# def containDuplicate(self, arr: list[int]) -> bool:
	# 	return len(arr) != len(set(arr))

	def containDuplicate(self, arr: list[int]) -> bool:
		seen = set()

		for num in arr:
			if num in seen:
				return True
			seen.add(num)

		return False


print(solution().containDuplicate([4,4,5,6,7,5,4]))
print(solution().containDuplicate([4,5,6,7]))
