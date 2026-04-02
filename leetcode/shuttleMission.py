# A space station network has two hubs: Alpha and Beta.

# Shuttles from Alpha → Beta take 100 time units and depart at times given in array alpha2beta (sorted).
# Shuttles from Beta → Alpha also take 100 time units and depart at times in array beta2alpha (sorted).
# You must complete missions, where each mission =
# Alpha → Beta → Alpha (round trip)

# You must always take the earliest possible shuttle available after your current time.

# Find the time when all missions are completed.

class solutions:
	def missionsCompleted(self, alpha2beta, beta2alpha, missions):
		currentTime = 0

		for i in range(missions):
			for j in range(len(alpha2beta)):
				if currentTime <= alpha2beta[j]:
					currentTime = alpha2beta[j] + 100
					break

			for k in range(len(beta2alpha)):
				if currentTime <= beta2alpha[k]:
					currentTime = beta2alpha[k] + 100
					break

		return currentTime

print(solutions().missionsCompleted([0, 200, 500], [99, 210, 450], 1))
print(solutions().missionsCompleted([0, 200, 500, 800], [150, 350, 650, 900], 3))
