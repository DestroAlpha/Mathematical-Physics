import numpy as np
import matplotlib.pyplot as plt
def cos_taylor(x, n):
    """
    Calculate the nth partial sum of the Taylor series for cos(x) at a given point x.
    """
    result = 0
    for i in range(n):
        result += (-1)*i * x*(2*i) / np.math.factorial(2*i)
    return result
x_values = np.linspace(-2*np.pi, 2*np.pi, 400)
n_values = [1, 2, 10, 20, 50]
plt.figure(figsize=(10, 6))
plt.plot(x_values, np.cos(x_values), label='cos(x)', color='blue')
for n in n_values:
    cos_approx = [cos_taylor(x, n) for x in x_values]
    plt.plot(x_values, cos_approx, label=f'n={n}')
plt.title('Approximation of cos(x) using Taylor series')
plt.xlabel('x')
plt.ylabel('Function value')
plt.legend()
plt.grid(True)
plt.show()
