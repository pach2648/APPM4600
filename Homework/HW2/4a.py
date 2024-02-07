import numpy as np

# create a vector 't' use np.arange(0,pi+pi/30,pi/30)
t = np.arange(0, (31/30)*np.pi, np.pi/30)

# create a vector 'y'
y = np.cos(t)

# Evaluate the sum using sum
S = np.sum(t*y)

# Evaluate the sum using for loop
S2 = 0 
for k in range(len(t)):
    S2 = S2 + t[k]*y[k]

print("The result from sum function is ", S)
print("The result from for loop is ", S2)
