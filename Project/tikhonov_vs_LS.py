import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_points = 100
x = np.linspace(0, 2*np.pi, num_points)
y_true = np.sin(x) + np.sin(5*x)
y_noisy = y_true + np.random.normal(0, 5, num_points)

# Plot the noisy data
plt.figure(figsize=(10, 6))
plt.scatter(x, y_noisy, color='blue', label='Noisy Data')

# Tikhonov Regularization
alpha = 5 # Regularization strength (lambda)
X = np.column_stack((np.sin(x), np.sin(5*x)))
I = np.eye(X.shape[1])
coefficients_tikhonov = np.linalg.inv(X.T @ X + alpha * I) @ X.T @ y_noisy
print(coefficients_tikhonov)

# Least squares solution
coefficients_least_squares = np.linalg.lstsq(X, y_noisy, rcond=None)[0]

# Predictions
y_pred_tikhonov = X @ coefficients_tikhonov
print(y_pred_tikhonov)
y_pred_least_squares = X @ coefficients_least_squares

# Plot the fitted curves
plt.plot(x, y_pred_tikhonov, color='red', label='Tikhonov Regularization')
plt.plot(x, y_pred_least_squares, color='green', label='Least Squares')
plt.plot(x, y_true, color='black', linestyle='--', label='True Function')
plt.legend()
plt.title('Comparison of Regression Models')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Compare derivatives
derivative_tikhonov = coefficients_tikhonov[0] + 5 * coefficients_tikhonov[1]
derivative_least_squares = coefficients_least_squares[0] + 5 * coefficients_least_squares[1]

print("Derivative using Tikhonov Regularization:", derivative_tikhonov)
print("Derivative using Least Squares Solution:", derivative_least_squares)
