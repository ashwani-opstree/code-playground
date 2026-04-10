"""  
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


class solution:
	def plus_one_mycode(self, nums: list) -> list:
		dec = 1
		val = 0

		for i in range(1, len(nums) + 1):
			val = nums[-i] * dec + val
			# print(val)
			dec *= 10
			
		p1 = val + 1
		result = [ int(digit) for digit in str(p1)]
		return result

	def plus_one(self, nums: list) -> list:
		for i in range(len(nums) - 1, -1, -1):
			if nums[i] < 9:
				nums[i] += 1
				return nums
			nums[i] = 0
		return [1] + nums


print(solution().plus_one([1,2,3,4]))
print(solution().plus_one([6,7,8,9]))