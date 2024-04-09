def cal_trapezoidal(a, b, f, N):
    """
    Parameters:
    a : Lower limit of the interval.
    b : Upper limit of the interval.
    f : The function f(x).
    N : Number of points.

    Returns:
    result: Summation from trapezoidal.
    """
    N_int = N - 1
    h = (b - a) / N_int # Step size
    result = f(a) + f(b)

    for i in range(1, N_int):
        k = a + i * h
        result += 2*f(k)

    return result * (h/2)

def cal_simpson(a, b, f, N):
    """
    Parameters:
    a : Lower limit of the interval.
    b : Upper limit of the interval.
    f : The function f(x).
    N : Number of point. *****N should be even.

    Returns:
    Result: Summation from simpson.
    """
    N_int = N - 1
    
    if N_int % 2 != 0:
        return print("Number of points (N) must be odd for Simpson's rule.")

    h = (b - a) / N_int # Step size
    result = f(a) + f(b)

    for i in range(1, N_int):
        k = a + i * h
        # Sum of even terms
        if i % 2 == 0:
            result += 2 * f(k)
        # Sum of odd terms
        else:
            result += 4 * f(k)

    return result * (h / 3)

# Main
def f(x):
    return x**2

a = 0
b = 1
N = 101
integral_approx_trapz = cal_trapezoidal(a, b, f, N)
print("Approximation of the integral using composite Trapezoidal rule:", integral_approx_trapz)

integral_approx_simpson = cal_simpson(a, b, f, N)
print("Approximation of the integral using composite Simpson's rule:", integral_approx_simpson)
