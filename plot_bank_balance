# D. M. Chakrabarti
# April 23 2026
# Plotting balance of bank account over time

import numpy as np
import matplotlib.pyplot as plt

# no withdraws over time period
# last date denoted T
# initial balance b_0
# interest rate r
# b_{t+1} = (1+r) b_t
# plot b_0,...,b_T

r = 0.025 # interest rate
T = 50 # end date
b = np.empty(T+1) # empty NumPy array to store all b_t
b[0] = 10 # initial balance

for t in range(T):
  b[t+1] = (1+r)*b[t]

plt.plot(b,label = 'bank account')
plt.legend()
plt.show()
