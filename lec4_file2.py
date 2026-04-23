# D. M. Chakrabarti
# April 23 2026
# random draws using user defined function
# return either standard normal or uniform random variables on (0,1)

import numpy as np
import matplotlib.pyplot as plt

def generate_data(n, generator_type):
  epsilon_values = []
  for i in range(n):
    if generator_type == 'uniform':
      e = np.random.uniform(0,1)
    else:
      e = np.random.randn()
    epsilon_values.append(e)
  return epsilon_values

data = generate_data(100, 'uniform')
plt.plot(data)
plt.show()
