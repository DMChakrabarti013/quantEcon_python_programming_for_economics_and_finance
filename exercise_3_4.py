# D. M. Chakrabarti
# April 23 2026
# Exercise 3.3
# Simulate and plot correlated time series

# x_{t+1} = \alpha |x_t| + \epsilon_{t+1}
# x_0 = 0
# t = 0,...T
# \epsilon_t IID
# do using if-else instead of abs

import numpy as np
import matplotlib.pyplot as plt

T = 200
alpha = 0.9
x = np.empty(T+1)
x[0] = 0

for t in range(T):
  if x[t] < 0:
    abs_x = -x[t]
  else:
    abs_x = x[t]
  x[t+1] = alpha * abs_x + np.random.randn()

plt.plot(x)
plt.show()
