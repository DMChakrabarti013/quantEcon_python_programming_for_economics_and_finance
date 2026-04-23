# D. M. Chakrabarti
# April 23 2026
# random draws using user defined function

import numpy as np
import matplotlib.pyplot as plt

def generate_data(n):
  epsilon_values = []
  for i in range(n):
    e = np.random.randn()
    epsilon_values.append(e)
  return epsilon_values

data = generate_data(100)
plt.plot(data)
plt.show()

