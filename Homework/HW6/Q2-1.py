import numpy as np
from scipy.integrate import quad

def cal_trapezoidal(a, b, f, N):
    """
    Parameters:
    a : Lower limit of the interval.
    b : Upper limit of the interval.
    f : The function f(x).
    N : Number of points.

    Returns:
    result: Summation from trapezoidal.
    """
    N_int = N - 1
    h = (b - a) / N_int # Step size
    result = f(a) + f(b)

    for i in range(1, N_int):
        k = a + i * h
        result += 2*f(k)

    return result * (h/2)

def cal_simpson(a, b, f, N):
    """
    Parameters:
    a : Lower limit of the interval.
    b : Upper limit of the interval.
    f : The function f(x).
    N : Number of point. *****N should be even.

    Returns:
    Result: Summation from simpson.
    """
    N_int = N - 1
    
    if N_int % 2 != 0:
        return print("Number of points (N) must be odd for Simpson's rule.")

    h = (b - a) / N_int # Step size
    result = f(a) + f(b)

    for i in range(1, N_int):
        k = a + i * h
        # Sum of even terms
        if i % 2 == 0:
            result += 2 * f(k)
        # Sum of odd terms
        else:
            result += 4 * f(k)

    return result * (h / 3)

# Main
def f(x):
    return 1 / (1 + x**2)

a = -5
b = 5
N = 1001
integral_approx_trapz = cal_trapezoidal(a, b, f, N)
print("Approximation of the integral using composite Trapezoidal rule:", integral_approx_trapz)

integral_approx_simpson = cal_simpson(a, b, f, N)
print("Approximation of the integral using composite Simpson's rule:", integral_approx_simpson)

# Error tolerances
tol = 1e-4

# Compute n for Trapezoidal rule
M2 = 2 # From hand calcualtion
n_trapezoidal = int(np.ceil(np.sqrt(((b - a)**3 * M2) / (12 * tol))))

# Compute n for Simpson's rule
M4 = 24 # From hand calcualtion
n_simpsons = int(np.ceil(np.power((b - a)**5 * M4 / (180 * tol), 1/4)))

error_trapezoidal = abs(2 * np.arctan(5) - integral_approx_trapz)
error_simpsons = abs(2 * np.arctan(5) - integral_approx_simpson)

# Print results
print("\nNumber of subintervals for Trapezoidal rule (n):", n_trapezoidal)
print("Error using composite Trapezoidal rule:", error_trapezoidal)

print("\nNumber of subintervals for Simpson's rule (n):", n_simpsons)
print("Error using composite Simpson's rule:", error_simpsons)

# Using quad from SciPy with default tolerance (1e-6)
result_default_tol = quad(f, a, b)
print("\nUsing quad with default tolerance (1e-6):")
print("Result:", result_default_tol[0])
print("Estimated error:", result_default_tol[1])

# Using quad from SciPy with tolerance set to 1e-4
result_1e4_tol = quad(f, a, b, epsabs=1e-4)
print("\nUsing quad with tolerance set to 1e-4:")
print("Result:", result_1e4_tol[0])
print("Estimated error:", result_1e4_tol[1])
