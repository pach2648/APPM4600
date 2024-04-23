import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def ridge_regression(X, y, alpha):
    # Add a column of ones to the X matrix for the intercept term
    X = np.column_stack((np.sin(X), np.sin(5*X)))
    
    # Calculate the coefficients using ridge regression formula
    n_features = X.shape[1]
    I = np.eye(n_features)
    beta = np.linalg.inv(X.T @ X + alpha * I) @ X.T @ y

    y_pred_tikhonov = X @ beta
    
    return y_pred_tikhonov

# Generate sample data
np.random.seed(0)
num_points = 100
x = np.linspace(0, 2, num_points)
f = lambda x: np.sin(x) + np.sin(5*x) #function
y_true = f(x)  # True function
noise = np.random.normal(0, 20, num_points)  # Gaussian noise
y_noisy = y_true + noise  # Noisy data

y_pred_tikhonov = ridge_regression(x,y_noisy,100)
y_pred_LS = ridge_regression(x,y_noisy,0)

# Plot the true function, noisy data, and fitted curve
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, label='True Function')
plt.scatter(x, y_noisy, color='red', label='Noisy Data')
plt.plot(x, y_pred_tikhonov, color='green', label='Tikhonov')
plt.plot(x, y_pred_LS, color='black', label='LS')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting')
plt.legend()
plt.grid(True)
plt.show()


