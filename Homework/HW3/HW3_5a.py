import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x)
def f(x):
    return x - 4 * np.sin(2 * x) - 3

# Generate x values
x_values = np.linspace(-2, 7.5, 1000)  # Adjust the range as needed

# Calculate corresponding y values
y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, label='$f(x)$')
plt.axhline(0, label='y = 0', color = 'black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of $f(x)$')
plt.legend()
plt.show()
