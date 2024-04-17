import numpy as np
import matplotlib.pyplot as plt
def func_sin(x):
    return np.sin(x)
def partial_sum_sin(x, n):
    result = 0
    for k in range(n + 1):
        coefficient = (-1)**k / np.math.factorial(2*k + 1)
        result += coefficient * x**(2*k + 1)
    return result
x_values = np.linspace(-2*np.pi, 2*np.pi, 400)
y_original = func_sin(x_values)
n_values = [1, 2, 5, 10]
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_original, label='Original Function: $sin(x)$', color='blue')
for n in n_values:
    y_partial_sum = [partial_sum_sin(x, n) for x in x_values]
    plt.plot(x_values, y_partial_sum, label=f'n={n}')
plt.title('Approximation of $sin(x)$ using Taylor Series')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
