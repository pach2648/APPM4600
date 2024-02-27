# Pre lab 6
import numpy as np

def f(x):
    return np.cos(x)

x_point = np.pi / 2

h = 0.01 * 2.**(-np.arange(0, 10))

# Forward difference method
f_diff_approx = (f(x_point + h) - f(x_point)) / h

# Centered Difference method
c_diff_approx = (f(x_point + h) - f(x_point - h)) / (2*h)

# Print the results
print("\n|__h__|__Forward Difference__|__Centered Difference__|")
print("-" * 55)
for i in range(len(h)):
    print(f"|__{h[i]:.10f}__|__{f_diff_approx[i]:.10f}__|__{c_diff_approx[i]:.10f}__|")


print("The order of forward difference method is the first-order")
print("The order of centered difference method is the second-order")
