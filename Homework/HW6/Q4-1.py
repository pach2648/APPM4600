import numpy as np
from scipy.special import gamma

def gamma_function_trapezoidal(t, a, b, n):
    """
    Compute the value of the gamma function using the composite trapezoidal rule.
    
    Parameters:
        t (float): Parameter of the gamma function.
        a (float): Lower limit of integration.
        b (float): Upper limit of integration.
        n (int): Number of subintervals for trapezoidal rule.
        
    Returns:
        float: Approximation of the gamma function.
    """
    # Step size
    h = (b - a) / n
    
    # Compute the function values at the endpoints
    fx0 = a**(t-1) * np.exp(-a)
    fxn = b**(t-1) * np.exp(-b)
    
    # Compute the sum of interior points
    sum_fx = sum((a + i*h)**(t-1) * np.exp(-a - i*h) for i in range(1, n))
    
    # Composite trapezoidal rule formula
    result = h * (0.5 * (fx0 + fxn) + sum_fx)
    
    return result

# Values of t to evaluate
values_of_t = [2, 4, 6, 8, 10]

# Lower and upper limits of integration
lower_limit = 0
upper_limit = 10  # Adjust this based on experimentation or analysis

# Number of subintervals for the trapezoidal rule
num_subintervals = 1000  # Adjust this based on experimentation or analysis

# Compute and compare the results
for t in values_of_t:
    # Compute using the trapezoidal rule
    trapezoidal_result = gamma_function_trapezoidal(t, lower_limit, upper_limit, num_subintervals)
    
    # Compute using scipy's gamma function
    scipy_result = gamma(t)
    
    # Print the results
    print(f"t={t}:")
    print("Trapezoidal Rule:", trapezoidal_result)
    print("Scipy's gamma function:", scipy_result)
    print("Relative Error:", abs(trapezoidal_result - scipy_result) / scipy_result)
    print()
