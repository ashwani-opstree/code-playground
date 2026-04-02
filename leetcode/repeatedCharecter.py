# Given a string s consisting of lowercase English letters, return the first letter to appear twice.

class solution:
	def repeatedCharecter(self, s: str) -> str:
		seen_letters = []

		for c in s:
			if c in seen_letters:
				return c
			else:
				seen_letters.append(c)

print(solution().repeatedCharecter("letters"))
