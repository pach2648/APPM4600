import numpy as np
import matplotlib.pyplot as plt

def construct_derivative_matrix(n):
    """
    Constructs the derivative matrix D for a vector function of length n.
    """
    D = np.zeros((n - 2, n))
    for i in range(n - 2):
        D[i, i] = -0.5
        D[i, i + 1] = 0
        D[i, i + 2] = 0.5
    return D

def tikhonov(x, y, lam, m):
    # Add a column of ones to the X matrix for the intercept term
    A = np.vstack((np.sin(x), np.sin(5*x), np.sin(10*x), np.sin(15*x))).T
    
    '''
    n = len(x) #number of interpolation points
    A = np.zeros([n,m+1])
    for i in range(m+1):
        for ii in range(n):
            A[ii,i] = x[ii]**i
    '''
    
    # Calculate the coefficients using tikhonov formula
    n_features = A.shape[1]
    I = np.eye(n_features)
    D = construct_derivative_matrix(n_features)
    coeff = np.linalg.inv(A.T @ A + lam**2 * D.T @ D) @ A.T @ y

    y_pred_tikhonov = A @ coeff
    
    return y_pred_tikhonov

# Generate sample data

D = construct_derivative_matrix(5)
print(D)

np.random.seed(0)
num_points = 100
x = np.linspace(0, 2*np.pi, num_points)
f = lambda x: np.sin(x) + np.sin(5*x) + np.sin(10*x) + np.sin(15*x) #function
y_true = f(x)  # True function
noise = np.random.normal(0, 0.1, num_points)  # Gaussian noise
y_noisy = y_true + noise  # Noisy data

m = 7

y_pred_tikhonov = tikhonov(x,y_noisy,100,m)
y_pred_LS = tikhonov(x,y_noisy,0,m)

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
