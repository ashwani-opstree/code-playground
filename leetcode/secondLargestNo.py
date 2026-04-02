# find the second lagest no. in the given array 

class solutions:
	def secondLargestNo(self, nums: list[int]) -> int:
		first = -1
		second = -1

		for num in nums:
			if first < num:
				second = first
				first = num
			elif second < num and num != second:
				second = num

		return second

print(solutions().secondLargestNo([4,40,5,14,20,50]))

print(solutions().secondLargestNo([4,1,3]))