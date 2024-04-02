import numpy as np
from scipy.special import legendre

def eval_legendre(n, x):
    # preallocate vector p with (n+1) zeros
    p = [0] * (n+1)
    # the first p is 1
    p[0] = 1
    # check n must be greater than 0
    if n > 0:
        # the second term of p is x
        p[1] = x
        for i in range(1, n):
            p[i+1] = (1/(i+1))*((2 * i+1) * x * p[i] - i * p[i-1])
    return p

# Test
n = 5
x = 0.5

legendre_mycode = eval_legendre(n, x)

print("Legendre polynomial values at x =", x)
print(legendre_mycode)
