import numpy as np
import matplotlib.pyplot as plt

# Function to calculate the manipulated expression
def manipulated_expression(x, delta):
    #return np.cos(x) * (np.cos(delta) - 1) - np.sin(x) * np.sin(delta)
    return -2 * (np.sin((2*x+delta)/2)) * (np.sin(delta/2))
    
# Values of x
x_values = [np.pi, 1e6]

# Values of delta
delta_values = np.logspace(-16, 0, num=17)

# Tabulate the differences for each combination of x and delta
differences = np.zeros(len(delta_values))
for x in x_values:
    for i in range(len(delta_values)):
        differences[i] = differences[i] +\
        abs(manipulated_expression(x, delta_values[i]) -\
        (np.cos(x + delta_values[i]) - np.cos(x)))
        print((f"Approximation for x = {x}, delta = {delta_values[i]}: {manipulated_expression(x, delta_values[i])}"))
    
    # Plot the differences
    plt.plot(np.log10(delta_values), differences, label=f'x = {x}')

# Add labels and legend
plt.xlabel("$log_{10} \\delta$")
plt.ylabel('Difference')
plt.legend(loc='upper left')
plt.title("Difference Between My Expression and $cos(x+\\delta)-cos(\\delta)$")
plt.show()
