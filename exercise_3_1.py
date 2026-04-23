# D. M. Chakrabarti
# April 23 2026
# Exercise 3.1
# Simulate and plot correlated time series

# x_{t+1} = \alpha x_t + \epsilon_t
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
  x[t+1] = alpha*x[t] + np.random.randn()

plt.plot(x)
plt.show()
