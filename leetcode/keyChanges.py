class Solutions:
	def keyChanges(self, recording: list[str]) -> int:

		count = 0
		for i in range(len(recording) - 1):
			if recording[i].upper() != recording[i +1].upper():
				count += 1

		return count

print(Solutions().keyChanges(['W', 'w', 'a', 'A', 'a', 'b', 'B']))