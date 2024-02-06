import matplotlib.pyplot as plt

# Define the polynomial function
def p(x):
    return (x - 2)**9

# Generate x values in the range [1.920, 2.080] with a step of 0.001
x_values = [i/1000 + 1.92 for i in range(161)]

# Evaluate the polynomial for each x value
y_values = [p(x) for x in x_values]

# Plot the polynomial
plt.plot(x_values, y_values, label='p(x) = $(x-2)^9$')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Plot of p(x) = $(x-2)^9$')
plt.legend()
plt.grid(True)
plt.show()
