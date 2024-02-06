import numpy as np
import numpy.linalg as la
import math

def driver():

    n = 100
    x = np.linspace(0,np.pi,n)

    #f = lambda x: x**2 + 4*x + 2*np.exp(x)
    #g = lambda x: 6*x**3 + 2*np.sin(x)

    # Two vectors tha
    f = lambda x: np.sin(2*x)
    g = lambda x: np.cos(2*x)

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

