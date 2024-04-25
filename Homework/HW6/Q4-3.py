import numpy as np
from scipy.special import gamma
from numpy.polynomial.laguerre import laggauss

def gamma_function_gauss_laguerre(t, n):
    """
    Compute the value of the gamma function using Gauss-Laguerre quadrature.
    
    Parameters:
        t : Parameter of the gamma function.
        n : Number of quadrature points.
        
    Returns:
        float: Approximation of the gamma function.
    """
    # Get the weights and abscissae for Gauss-Laguerre quadrature
    x, w = laggauss(n)
    
    # Compute the approximation of the gamma function
    gamma_approx = np.sum(w * x**(t-1))
    
    return gamma_approx

# Values of t to evaluate
values_of_t = [2, 4, 6, 8, 10]

# Number of quadrature points
n = 57  # Adjust this based on desired accuracy

# Compute and compare the results
for t in values_of_t:
    # Compute using Gauss-Laguerre quadrature
    gauss_laguerre_result = gamma_function_gauss_laguerre(t, n)
    
    # Compute using scipy's gamma function
    scipy_result = gamma(t)
    
    # Print the results
    print(f"t={t}:")
    print("Gauss-Laguerre Quadrature:", gauss_laguerre_result)
    print("Scipy's gamma function:", scipy_result)
    print("Relative Error:", abs(gauss_laguerre_result - scipy_result) / scipy_result)
    print()
