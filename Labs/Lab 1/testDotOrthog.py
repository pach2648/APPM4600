import numpy as np
import numpy.linalg as la
import math

def driver():

    n = 100
    x = np.linspace(0,np.pi,n)

    # Two vectors that are otthogonal
    f = lambda x: np.sin(x)
    g = lambda x: np.cos(x)

    y = f(x)
    w = g(x)

    dp = dotProduct(y,w,len(y))

    print("The dot product is : ", dp)

    return

def dotProduct(x,y,n):
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]

    return dp

driver()

