# Pascal Triangle

class solution:
	def pascalTriangle(self, numRows: int) -> list[list[int]]:
		first_row = [1]
		rows = [first_row]

		for _ in range(1, numRows):
			row = [1]
			for i in range(1, len(rows[-1])):
				num = rows[-1][i-1] + rows[-1][i]
				row.append(num)
			row.append(1)
			rows.append(row)

		return rows

print(solution().pascalTriangle(10))