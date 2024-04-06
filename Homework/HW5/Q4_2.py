import numpy as np
import matplotlib.pyplot as plt

# Data points
x = np.array([0, 1, 2, 3])
y = np.array([1, 4, 2, 6])

# Coefficients for weighted least squares line
a0_weighted = 1.2573
a1_weighted = 1.2427

# Original line without weights (least squares)
a0_unweighted = 1.3
a1_unweighted = 1.3

# Generate points for the lines
x_values = np.linspace(0, 3, 100)
y_weighted = a1_weighted * x_values + a0_weighted
y_unweighted = a1_unweighted * x_values + a0_unweighted

# Plotting the data points and lines
plt.scatter(x, y, label='Data points')
plt.plot(x_values, y_weighted, label='Weighted least squares line', color='red')
plt.plot(x_values, y_unweighted, label='Least squares line (unweighted)', linestyle='dashed', color='green')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Weighted and Unweighted Least Squares Fit')
plt.legend()
plt.grid(True)
plt.show()
