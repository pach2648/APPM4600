import numpy as np
import math

x = 9.999999995000000*10**(-10)

result = x + (x**2)/math.factorial(2)
print(result)
