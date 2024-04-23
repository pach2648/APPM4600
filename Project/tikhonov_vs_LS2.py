import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(0)
num_points = 100
x = np.linspace(0, 2*np.pi, num_points)
y_true = np.sin(x) + np.sin(5*x)  # True function
noise = np.random.normal(0, 0.1, num_points)  # Gaussian noise
y_noisy = y_true + noise  # Noisy data

# Plot the original curve and the noisy data
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, label='True Function')
plt.scatter(x, y_noisy, color='red', label='Noisy Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('True Function and Noisy Data')
plt.legend()
plt.grid(True)
plt.show()

# Implement Tikhonov regularization
alpha = 0.1  # Regularization strength (lambda)
X = np.column_stack((np.sin(x), np.sin(5*x)))  # Design matrix
alpha_matrix = alpha * np.eye(X.shape[1])  # Regularization matrix
coefficients = np.linalg.inv(X.T @ X + alpha_matrix) @ X.T @ y_noisy

# Calculate predictions
y_tikhonov = X @ coefficients

# Plot the Tikhonov regularization fit
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, label='True Function')
plt.plot(x, y_tikhonov, color='green', label='Tikhonov Regularization Fit')
plt.scatter(x, y_noisy, color='red', label='Noisy Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tikhonov Regularization Fit')
plt.legend()
plt.grid(True)
plt.show()
