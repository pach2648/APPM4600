import numpy as np
import matplotlib.pyplot as plt

# Define the true function
def true_function(x):
    return np.sin(x) + np.sin(5*x)

# Generate noisy data
np.random.seed(0)
n = 100
x = np.linspace(0, np.pi, n)
y_true = true_function(x)
noise = np.random.normal(0, 5, size=y_true.shape)
y_noisy = y_true + noise

# Perform Tikhonov regularization manually
def tikhonov_regularization(x, y, lam):
    A = np.column_stack((np.ones_like(x), np.sin(x), np.sin(2*x),np.sin(3*x),np.sin(4*x),np.sin(5*x),np.sin(6*x),np.sin(7*x),np.sin(8*x),np.sin(9*x),np.sin(10*x)))
    lam_matrix = lam**2 * np.eye(A.shape[1])  # Regularization matrix
    TN_coefficients = np.linalg.inv(A.T @ A + lam_matrix) @ A.T @ y
    y_tikhonov = A @ TN_coefficients
    return y_tikhonov,TN_coefficients

# Perform ordinary least squares regression
def ordinary_least_squares(x, y):
    A = np.column_stack((np.ones_like(x), np.sin(x), np.sin(2*x),np.sin(3*x),np.sin(4*x),np.sin(5*x),np.sin(6*x),np.sin(7*x),np.sin(8*x),np.sin(9*x),np.sin(10*x)))
    OLS_coefficients = np.linalg.inv(A.T @ A) @ A.T @ y
    y_OLS = A @ OLS_coefficients
    return y_OLS, OLS_coefficients

# Find the max and min position in a list
def min_max_position(lst):
    arr = np.array(lst)
    min_pos = np.argmin(arr) + 1
    max_pos = np.argmax(arr) + 1

    return min_pos, max_pos

#################################

# Define the range of alpha values
lams = np.linspace(0, 50, 1000)
errors_tik = []
errors_ols = []

# Calculate errors for each alpha
for lam in lams:
    y_tik,tik_coefficients = tikhonov_regularization(x, y_noisy, lam)
    y_ols,OLS_coefficients = ordinary_least_squares(x, y_noisy)
    error_tik = np.mean((y_true - y_tik)**2)
    error_ols = np.mean((y_true - y_ols)**2)
    errors_tik.append(error_tik)
    errors_ols.append(error_ols)

# Find the position of the min value of mean square error
min_pos, max_pos = min_max_position(errors_tik)

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

###################################

# Define the Tikhonov regularization parameter (Lambda) (From error analysis)
lam = lams[min_pos]
print("The value of lambda is", lam)

# Perform Tikhonov regularization
y_tik,tik_coefficients = tikhonov_regularization(x, y_noisy, lam)
print(tik_coefficients)

# Perform ordinary least squares regression
y_ols,OLS_coefficients = ordinary_least_squares(x, y_noisy)
print(OLS_coefficients)

# Plot the solutions
plt.figure(figsize=(8, 6))
plt.plot(x, y_true, label='True Function')
plt.scatter(x, y_noisy, color='red', label='Noisy Data')
plt.plot(x, y_tik, label='Tikhonov Regularization', linestyle='--')
plt.plot(x, y_ols, label='Ordinary Least Squares', linestyle='--')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Solutions')
plt.show()
