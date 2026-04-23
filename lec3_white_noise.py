# D. M. Chakrabarti
# April 22 2026

# Plotting a white noise process
import numpy as np
import matplotlib.pyplot as plt

epsilon_values = np.random.randn(100)
plt.plot(epsilon_values)
plt.show()

# Plotting using a for loop
ts_length = 100
epsilon_values = [] # empty list

for i in range(ts_length):
  e = np.random.randn()
  epsilon_values.append(e)

plt.plot(epsilon_values)
plt.show()

# Plotting using a while loop
ts_length = 100
epsilon_values = []
i = 0

while i < ts_length:
  e = np.random.randn()
  epsilon_values.append(e)
  i = i+1

plt.plot(epsilon_values)
plt.plot()
