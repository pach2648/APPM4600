import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

# Define the periodic function f(x) = sin(9x)
f = lambda x: np.sin(9*x)
a = 0  # Start of interval
b = 1  # End of interval

# Number of equispaced points for interpolation
n_values = [5, 10, 20, 40]

for n in n_values:
    # Generate equispaced points
    x_int = np.linspace(a, b, n)
    y_int = f(x_int)

    # Create exact values
    x_eval = np.linspace(a, b, 1000)
    y_exact = f(x_eval)

    # Interpolate using periodic cubic splines
    cs = CubicSpline(x_int, y_int)
    y_interp = cs(x_eval)

    # Compute interpolation error
    error = np.abs(y_exact - y_interp)

    # Plot the logarithm of the interpolation error
    plt.figure()
    plt.plot(x_eval, np.log10(error))
    plt.title(f"Logarithm of Error (n = {n})")
    plt.xlabel("x")
    plt.ylabel("Log10(Error)")
    plt.grid(True)
    plt.show()

