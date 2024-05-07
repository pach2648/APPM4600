import numpy as np
import matplotlib.pyplot as plt

def derivative_matrix(n):
    """
    Constructs the derivative matrix D for a vector function of length n.
    """
    D = np.zeros((n-2, n))
    for i in range(n - 2):
        D[i, i] = -0.5
        D[i, i + 1] = 0
        D[i, i + 2] = 0.5
    return D

def construct_derivative_matrix_svd(n):
    """
    Constructs the derivative matrix D using singular value decomposition (SVD).
    """
    # Construct the difference matrix
    M = np.eye(n) - np.roll(np.eye(n), -1, axis=1)
    
    # Perform SVD on the difference matrix
    U, s, Vh = np.linalg.svd(M)
    
    # Determine the number of singular values to use
    k = 2  # Number of smallest singular values to use (can be adjusted)
    
    # Construct the derivative matrix using singular vectors corresponding to the smallest singular values
    D = np.dot(U[:, -k:], np.dot(np.diag(s[-k:]), Vh[-k:, :]))
    
    return D

def construct_D_matrix_svd(A, k):
    """
    Constructs the D matrix using singular value decomposition (SVD).
    """
    # Perform SVD on the design matrix A
    U, s, Vt = np.linalg.svd(A)
    
    # Use the singular vectors corresponding to the smallest singular values to construct D
    D = U[:, -k:]
    
    return D


def tikhonov(A, y, lam):
    # Calculate the coefficients using tikhonov formula
    n_features = A.shape[1]
    I = np.eye(n_features)
    D = construct_D_matrix_svd(A, n_features)
    #D = derivative_matrix(n_features)
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

# Find the max and min position in a list
def min_max_position(lst):
    arr = np.array(lst)
    min_pos = np.argmin(arr) + 1
    max_pos = np.argmax(arr) + 1

    return min_pos, max_pos

# Generate sample data
np.random.seed(0)
num_points = 100
x = np.linspace(0, np.pi, num_points)
# function
f = lambda x: np.sin(x) + np.sin(5*x)
#f = lambda x: np.sin(x) + np.sin(5*x)
# True function
y_true = f(x)  
# Gaussian noise
noise = np.random.normal(0, 2, num_points)
# Noisy data
y_noisy = y_true + noise
# A matrix
A = np.column_stack((np.sin(x),np.sin(2*x),np.sin(3*x),np.sin(4*x),np.sin(5*x),np.sin(6*x),np.sin(7*x),np.sin(8*x),np.sin(9*x),np.sin(10*x)))
#A = np.column_stack((np.sin(x), np.sin(5*x)))

####################################
# Define the range of alpha values
lams = np.linspace(0, 50, 100)
errors_tik = []
errors_ols = []
errors_ridge = []

# Calculate errors for each alpha
for lam in lams:
    
    y_tik = tikhonov(A,y_noisy,lam)
    y_ols = ridge_regression(A,y_noisy,0)
    y_ridge = ridge_regression(A,y_noisy,lam)
    error_tik = np.mean((y_true - y_tik)**2)
    error_ols = np.mean((y_true - y_ols)**2)
    error_ridge = np.mean((y_true - y_ridge)**2)
    errors_tik.append(error_tik)
    errors_ols.append(error_ols)
    errors_ridge.append(error_ridge)

# Find the position of the min value of mean square error
min_pos, max_pos = min_max_position(errors_tik)

# Plot the error comparison
plt.figure(figsize=(8, 6))
plt.plot(lams, errors_tik, label='Tikhonov Regularization')
plt.plot(lams, errors_ols, label='Ordinary Least Squares')
#plt.plot(lams, errors_ridge, label='Ridge Regression')
plt.xlabel('Lambda')
plt.ylabel('Mean Squared Error')
plt.title('Error Comparison')
plt.legend()
plt.grid(True)
plt.show()

####################################

print("The lambda we choose is:",lams[min_pos])

y_pred_tikhonov = tikhonov(A,y_noisy,lam = lams[min_pos])
y_pred_LS = ridge_regression(A,y_noisy,0)
y_pred_ridge = ridge_regression(A, y_noisy, lams[min_pos])

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

print("Mean Squared Error (Tikhonov Regularization):",np.mean(err_tikhonov)**2)
print("Mean Squared Error (Least Squares):",np.mean(err_LS)**2)
print("Mean Squared Error (LRidge Regression):",np.mean(err_ridge)**2)
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

'''
# Define the range of alpha values
lams = np.linspace(0, 50, 100)
errors_tik = []
errors_ols = []

# Calculate errors for each alpha
for lam in lams:
    
    y_tik = tikhonov(A,y_noisy,lam)
    y_ols = ridge_regression(A,y_noisy,0)
    error_tik = np.mean((y_true - y_tik)**2)
    error_ols = np.mean((y_true - y_ols)**2)
    errors_tik.append(error_tik)
    errors_ols.append(error_ols)

# Find the position of the min value of mean square error
min_pos, max_pos = min_max_position(errors_tik)
print(max_pos)
'''
'''
# Plot the error comparison
plt.figure(figsize=(8, 6))
plt.plot(lams, errors_tik, label='Tikhonov Regularization')
plt.plot(lams, errors_ols, label='Ordinary Least Squares')
plt.xlabel('Lambda')
plt.ylabel('Mean Squared Error')
plt.title('Error Comparison')
plt.legend()
plt.grid(True)
plt.show()
'''
