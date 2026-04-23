# D. M. Chakrabarti
# April 23 2026
# Exercise 3.2
# following 3.1
# Simulate and plot correlated time series

# x_{t+1} = \alpha x_t + \epsilon_t
# x_0 = 0
# t = 0,...T
# \epsilon_t IID

import numpy as np
import matplotlib.pyplot as plt

T = 200
alpha_values = [0, 0.8, 0.98]
x = np.empty(T+1)

for alpha in alpha_values:
  x[0] = 0
  for t in range(T):
    x[t+1] = alpha*x[t] + np.random.randn()
  plt.plot(x, label=f'$\\alpha = {alpha}$')

plt.legend()
plt.show()
