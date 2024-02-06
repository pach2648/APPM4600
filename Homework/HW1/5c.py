import numpy as np

# Function to compute the derivative of cos(x) at a point x
def derivative_cos(x):
    h = 1e-6
    return (np.cos(x + h) - np.cos(x - h)) / (2 * h)

# Function to compute the second derivative of cos(x) at a point x
def second_derivative_cos(x):
    h = 1e-6
    return (np.cos(x + h) - 2 * np.cos(x) + np.cos(x - h)) / (h ** 2)

# Function to approximate cos(x + delta) - cos(x) using Taylor expansion
def taylor_approximation_cos(x, delta):
    f_prime_x = derivative_cos(x)
    f_double_prime_xi = second_derivative_cos(x + delta)
    return delta * f_prime_x + (delta ** 2) / 2 * f_double_prime_xi

# Values of x and delta
x_values = [np.pi, 1e6]
delta_values = [1e-16, 1e-15, 1e-14, 1e-13, 1e-12, 1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1]

# Compute and print the approximations using the Taylor expansion
for x in x_values:
    print(f"For x = {x}:")
    for delta in delta_values:
        approx = taylor_approximation_cos(x, delta)
        print(f"Delta = {delta}: Approximation = {approx}")

