import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def p(x):
    return x**9-18*x**8+144*x**7-672*x**6+2016*x**5-4032*x**4+5376*x**3-4608*x**2+2304*x-512

def p2(x):
    return (x - 2)**9

# Define the range of x values
x_values = np.arange(1.92, 2.080, 0.001)

# Evaluate the polynomial for each x value
p_values = np.zeros(len(x_values))
for i in range(len(x_values)):
    p_values[i] = p_values[i] + p(x_values[i])
print((f"Approx = {p_values}"))
    
#p_values = [p(x) for x in x_values] ##another method (easier)

#########################

# Evaluate the polynomial for each x value
p_values2 = np.zeros(len(x_values))
for i in range(len(x_values)):
    p_values2[i] = p_values2[i] + p2(x_values[i])
print((f"Correc = {p_values2}"))

#p_values2 = [p2(x) for x in x_values] ##another method (easier)

# Plot the polynomial
plt.plot(x_values, p_values, label='p via its coefficients')
plt.plot(x_values, p_values2, label='p via expression')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title('Plot of p(x)')
plt.legend()
plt.grid(True)
plt.show()
