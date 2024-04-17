import numpy as np
import matplotlib.pyplot as plt
def log_taylor(x, n):
    """
    Calculate the nth partial sum of the Taylor series for log(1 + x) at a given point x.
    """
    result = 0
    for i in range(1, n+1):
        result += (-1)*(i+1) * (x*i) / i
    return result
x_values = np.linspace(-0.9, 1, 400)
n_values = [1, 2, 10, 50, 100]
plt.figure(figsize=(10, 6))
plt.plot(x_values, np.log(1 + x_values), label='log(1 + x)', color='blue')
for n in n_values:
    log_approx = [log_taylor(x, n) for x in x_values]
    plt.plot(x_values, log_approx, label=f'n={n}')

plt.title('Approximation of log(1 + x) using Taylor series')
plt.xlabel('x')
plt.ylabel('Function value')
plt.legend()
plt.grid(True)
plt.show()
