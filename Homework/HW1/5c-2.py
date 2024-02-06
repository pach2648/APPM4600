import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the aprroximation from Taylor formula
def approx_cos_difference(x, delta):
    """
    Approximates cos(x + delta) - cos(x) using Taylor expansion.

    Inputs:
    x : Value of x.
    delta : Value of delta.

    Outputs:
    approximation : Approximation of cos(x + delta) - cos(x).
    """
    # Calculate the approximation
    approximation = -delta * np.sin(x) - 0.5 * delta**2 * np.cos(delta)

    return approximation

# Function to calculate the manipulated expression
def manipulated_expression(x, delta):
    #return np.cos(x) * (np.cos(delta) - 1) - np.sin(x) * np.sin(delta)
    return -2 * (np.sin((2*x+delta)/2)) * (np.sin(delta/2))

# Test the function
x_values = [np.pi, 1e6]

# Values of delta
delta_values = np.logspace(-16, 0, num=17)

differences = np.zeros(len(delta_values))
for x in x_values:
    for i in range(len(delta_values)):
        approximation_taylor = approx_cos_difference(x, delta_values[i])
        manipulated = manipulated_expression(x, delta_values[i])
        differences[i] = differences[i] + abs(approximation_taylor - manipulated)
        print(f"Differences for x = {x}, delta = {delta_values[i]}: {abs(approximation_taylor - manipulated)}")

    plt.plot(np.log10(delta_values), differences, label=f'x = {x}')

# Add labels and legend
plt.xlabel("$log_{10} \\delta$")
plt.ylabel('Difference')
plt.legend(loc='upper left')
plt.title("Difference Between Approximation and Manipulated Values of $cos(x+\\delta)-cos(\\delta)$")
plt.show()    
