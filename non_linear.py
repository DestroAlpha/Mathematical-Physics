#AIM:-Find the root of non-linear equation x**3+4*x+9 using Newton Raphson Method

import math

#Define the function
def f(x):
    return x**3+4*x+9

#Define the Derivative of the function
def df(x):
    return 3*(x**2)+4
#Initial guess 
x0=1.0

#Tolerance
tol=1e-6

#Maximum number of iterations
max_iter = 100

#Newton-Raphson method
for i in range(max_iter):
    x1= x0 - f(x0)/df(x0)
    if abs(x1-x0) <tol:
        break
    x0=x1
print('The solution:',x1)