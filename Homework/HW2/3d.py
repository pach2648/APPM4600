import numpy as np
import math

x = 9.999999995000000*10**(-10)

LHS = 10**(-16)*10**(-9)

# Find number of n that make LHS(abs_err) > RHS(taylor_err)
for n in range(100):
    RHS = ((math.exp(x))*x**(n+1))/(math.factorial(n+1))
    if LHS > RHS:
        print("Number of n is ", n)
        break
    
