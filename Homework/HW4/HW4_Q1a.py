import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
import time

def f(x, y):
    return 3*x**2 - y**2

def g(x, y):
    return 3*x*y**2 - x**3 - 1

def iterate(x, y):
    dx = (1/6 * f(x,y)) + (1/18 * g(x,y))
    dy = 1/6 * g(x,y)
    x_nn = x - dx
    y_nn = y - dy
    return x_nn, y_nn

##############################
# Initial Values x_0 and y_0
x0 = 1
y0 = 1

# Max iterations
N = 1000
tol = 1e-10


# While loop
iterations = 0
t = time.time()
while iterations < N:
    x1, y1 = iterate(x0, y0)
    
    # Check for convergence
    if abs(x1 - x0) < tol and abs(y1 - y0) < tol:
        print("Converge to solution: x = ",x1," y = ",y1)
        print("Iterations: ", iterations)
        elapsed = time.time()-t;
        print(elapsed)
        break
    
    # Update values for the next iteration
    x0 = x1
    y0 = y1
    iterations = iterations + 1
else:
    print("Diverge within the number of N")

