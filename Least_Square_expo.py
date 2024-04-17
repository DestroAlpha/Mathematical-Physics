import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.3, 3.5, 6.1, 8.4, 12.1]) 
Y = np.log(y)
A, b = np.polyfit(x, Y, 1)
a = np.exp(A)
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a * np.exp(b * x_fit)

plt.scatter(x, y, label='Original data')
plt.plot(x_fit, y_fit, 'r', label='Fitted curve: y = {:.2f} * exp({:.2f} * x)'.format(a, b))
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Exponential Least Squares Fitting')
plt.grid(True)
plt.show()
