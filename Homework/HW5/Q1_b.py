import numpy as np
import matplotlib.pyplot as plt

def barycentric_lagrange_interpolation(x, y, z):
    n = len(x) - 1
    m = len(z)
    p = np.zeros(m)

    for j in range(m):
        weighted_sum_num = 0
        weighted_sum_denom = 0
        for k in range(n + 1):
            w = 1 #start at 1 since it is the product not the sum
            for i in range(n + 1):
                if i != k:
                    w *= 1 / (x[k] - x[i])
            weighted_sum_num += w * y[k] / (z[j] - x[k])
            weighted_sum_denom += w / (z[j] - x[k])
        p[j] = weighted_sum_num / weighted_sum_denom

    return p

def f(x):
    return 1 / (1 + (16 * x) ** 2)

#########################
#Main

n_values = [2, 3, 4, 5]
x_plot = np.linspace(-1, 1, 1001)
f_plot = f(x_plot)

for n in n_values:
    h = 2 / n
    x_interpolation = np.array([-1 + (i - 1) * h for i in range(1, n + 2)])
    y_interpolation = f(x_interpolation)

    p_x_plot = barycentric_lagrange_interpolation(x_interpolation, y_interpolation, x_plot)

    plt.plot(x_plot, p_x_plot, label=f'n = {n}')

plt.plot(x_plot, f_plot, label='f(x)')
plt.plot(x_interpolation, y_interpolation, 'o', label='Interpolation Points')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Barycentric Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()

n_values_2 = [15,16,17,18,19,20]
for n in n_values_2:
    h = 2 / n
    x_interpolation = np.array([-1 + (i - 1) * h for i in range(1, n + 2)])
    y_interpolation = f(x_interpolation)

    p_x_plot = barycentric_lagrange_interpolation(x_interpolation, y_interpolation, x_plot)

    plt.plot(x_plot, p_x_plot, label=f'n = {n}')

plt.plot(x_plot, f_plot, label='f(x)')
plt.plot(x_interpolation, y_interpolation, 'o', label='Interpolation Points')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Barycentric Lagrange Interpolation')
plt.legend()
plt.grid(True)
plt.show()

