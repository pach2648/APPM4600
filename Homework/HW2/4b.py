import numpy as np
import matplotlib.pyplot as plt
import random

#########
# Given parameters
n = 10000
theta = np.linspace(0, 2*np.pi, n)
R = 1.2
delta_r = 0.1
f = 15
p = 0

# Parametric curves
x = R*(1 + delta_r*np.sin(f*theta + p))*np.cos(theta)
y = R*(1 + delta_r*np.sin(f*theta + p))*np.sin(theta)

# Plot the curve
plt.plot(x,y)
plt.title("The First Parametric Curve")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#########
# Use for loop to plot 10 curves
for i in range(1,11):
    #Given parameters
    R = i
    delta_r = 0.05
    f = 2 + i
    p = random.uniform(0,2)

    x = R*(1 + delta_r*np.sin(f*theta + p))*np.cos(theta)
    y = R*(1 + delta_r*np.sin(f*theta + p))*np.sin(theta)

    plt.plot(x, y, label=f'i={i}')

plt.title("The Second Parametric Curve")
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.show()
