# Complete the function to return the respective number of the century
import math
def century(year):
  toString = str(year)
  if int(toString[-1:]) == 0:
    cent = int(toString[:-2]) 
    return cent
  else:
    cent = int(toString[:2]) + 1
    return cent


# Invoke the function with any given year
print(century(2001))
