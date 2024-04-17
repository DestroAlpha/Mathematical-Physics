import numpy as np
import matplotlib.pyplot as plt
import math
def func_exp(x):
  return np.exp(x)
def partial_sum_exp(x, n):
  result = 0
  for k in range(n + 1):
         result += x**k / math.factorial(k)
         return result
x_values = np.linspace(-2, 2, 400)
y_original = func_exp(x_values)
n_values = [1, 2, 5, 10]
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_original, label='Original Function: $e^x$', color='blue')
for n in n_values:
     y_partial_sum = [partial_sum_exp(x, n) for x in x_values]
     plt.plot(x_values, y_partial_sum, label=f'n={n}')
plt.title('Approximation of $e^x$ using Taylor Series')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
