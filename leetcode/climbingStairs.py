class solution: 
	def climbingStairs(self, stairts: int) -> int:
		if stairts <= 2:
			return stairts

		ways = [0] * (stairts + 1)
		ways[1] = 1
		ways[2] = 2
		
        for i in range(3, stairts + 1):
		   ways[i] = ways[i - 1] + ways[i - 2]

        return ways[stairts]

print(solution().climbingStairs(5))