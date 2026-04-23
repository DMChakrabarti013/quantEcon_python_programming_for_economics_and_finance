# D. M. Chakrabarti
# April 23 2026
# Exercise 3.3
# Approximation of pi using monte carlo

n = 1000000

count = 0
for i in range(n):
  u = np.random.uniform()
  v = np.random.uniform()

  d = np.sqrt((u - 0.5)**2 + (v-0.5)**2)

  if d < 0.5:
    count = count + 1

area_estimate = count/n

print(4*area_estimate)

