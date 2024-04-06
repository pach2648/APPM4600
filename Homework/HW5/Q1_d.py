import numpy as np
import matplotlib.pyplot as plt

def chebyshev_nodes(n):
    return np.cos((2 * np.arange(n + 1) + 1) * np.pi / (2 * (n + 1)))

def psi_n(x, n, nodes):
    psi = np.ones_like(x)
    for i in nodes:
        psi *= (x - i)
    return np.abs(psi)

n_values = [20]
x_plot = np.linspace(-1, 1, 1001)

for n in n_values:
    x_equispaced = np.linspace(-1, 1, n + 1)
    x_chebyshev = chebyshev_nodes(n)
    
    psi_equispaced = psi_n(x_plot, n, x_equispaced)
    psi_chebyshev = psi_n(x_plot, n, x_chebyshev)
    
    plt.plot(x_plot, np.log10(psi_equispaced), label=f'Equispaced, n = {n}')
    plt.plot(x_plot, np.log10(psi_chebyshev), label=f'Chebyshev, n = {n}')

plt.xlabel('x')
plt.ylabel('log10(Psi_n(x))')
plt.title('Comparison of Interpolation Error for Equispaced and Chebyshev Nodes')
plt.legend()
plt.grid(True)
plt.show()
