# D. M. Chakrabarti
# April 23 2026
# exercise 4.1
# write a function to compute factorial

def factorial(n):
  f = 1
  while n > 1:
    f *= n
    n -= 1
  return f

factorial(4)



