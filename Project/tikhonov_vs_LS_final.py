import numpy as np
import matplotlib.pyplot as plt

def derivative_matrix(n):
    """
    Constructs the derivative matrix D for a vector function of length n.
    """
    D = np.zeros((n - 2, n))
    for i in range(n - 2):
        D[i, i] = -0.5
        D[i, i + 1] = 0
        D[i, i + 2] = 0.5
    return D

def tikhonov(A, y, lam):
    # Calculate the coefficients using tikhonov formula
    n_features = A.shape[1]
    I = np.eye(n_features)
    D = derivative_matrix(n_features)
    x = np.linalg.inv(A.T @ A + lam**2 * D.T @ D) @ A.T @ y

    y_pred_tikhonov = A @ x
    
    return y_pred_tikhonov

def ridge_regression(A, y, lam):
    # Calculate the coefficients using tikhonov formula
    n_features = A.shape[1]
    I = np.eye(n_features)
    x = np.linalg.inv(A.T @ A + lam * I) @ A.T @ y

    y_pred_ridge = A @ x
    
    return y_pred_ridge

# Generate sample data

D = derivative_matrix(n = 6)
print(D)

np.random.seed(0)
num_points = 100
x = np.linspace(0, np.pi, num_points)
# function
f = lambda x: np.sin(x) + np.sin(5*x) + np.sin(10*x) + np.sin(15*x)
f = lambda x: np.sin(x) + np.sin(5*x)
# True function
y_true = f(x)  
# Gaussian noise
noise = np.random.normal(0, 2, num_points)
# Noisy data
y_noisy = y_true + noise
# A matrix
A = np.column_stack((np.sin(x), np.sin(5*x), np.sin(10*x), np.sin(15*x)))
A = np.column_stack((np.sin(x), np.sin(5*x)))

y_pred_tikhonov = tikhonov(A,y_noisy,lam = 10)
y_pred_LS = ridge_regression(A,y_noisy,0)
y_pred_ridge = ridge_regression(A, y_noisy, lam = 10)

# Plot the true function, noisy data, and fitted curve
plt.figure(figsize=(10, 6))
plt.plot(x, y_true, label='True Function')
plt.scatter(x, y_noisy, color='red', label='Noisy Data')
plt.plot(x, y_pred_tikhonov, color='green', label='Tikhonov')
plt.plot(x, y_pred_LS, color='black', label='LS')
plt.plot(x, y_pred_ridge, color='purple', label='Ridge')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting')
plt.legend()
plt.grid(True)
plt.show()

err_tikhonov = abs(y_pred_tikhonov - y_true)
err_LS = abs(y_pred_LS - y_true)
err_ridge = abs(y_pred_ridge - y_true)
print("Average Absolute Error (Tikhonov Regularization):",np.mean(err_tikhonov))
print("Average Absolute Error (Least Squares):",np.mean(err_LS))
print("Average Absolute Error (LRidge Regression):",np.mean(err_ridge))
plt.figure(figsize=(10, 6))
plt.plot(x, err_tikhonov, color='green', label='Tikhonov')
plt.plot(x, err_LS, color='black', label='LS')
plt.plot(x, err_ridge, color='purple', label='Ridge')
plt.xlabel('x')
plt.ylabel('Absolute Error')
plt.title('Error Comparison')
plt.legend()
plt.grid(True)
plt.show()

