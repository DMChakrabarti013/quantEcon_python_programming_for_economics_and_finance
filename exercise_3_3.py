# D. M. Chakrabarti
# April 23 2026
# Exercise 3.3
# Simulate and plot correlated time series

# x_{t+1} = \alpha |x_t| + \epsilon_{t+1}
# x_0 = 0
# t = 0,...T
# \epsilon_t IID

import numpy as np
import matplotlib.pyplot as plt

T = 200
alpha = 0.9
x = np.empty(T+1)
x[0] = 0

for t in range(T):
  x[t+1] = alpha * np.abs(x[t]) + np.random.randn()

plt.plot(x)
plt.show()
