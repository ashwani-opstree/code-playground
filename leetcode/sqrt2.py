class solution:
	def sqrt(self, x :int) -> int:
		if x <= 2:
			return x 
		L, R = 1, x

		while L <= R:
			M = (L + R) // 2
			square_M = M * M 

			if x == square_M:
				return M 
			elif x < square_M:
				R = R -1
			else:
				L = L + 1

print(solution().sqrt(81))
