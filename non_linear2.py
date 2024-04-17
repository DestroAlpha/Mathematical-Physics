#AIM:- Find the root of non-linear equation 2*x**3-2*x-5 using Newton Raphson Method
 
import math

#Define the  function
def f(x):
    return 2*x**3-2*x-5

#Define the derivative of the function
def df(x):
    return 6*(x**2)-2

#1nitial guess
x0=1.0
#Tolerance
tol=1e-6

#Maximum number of iterations
max_iter = 100

#Newton-Raphson method
for i in range(max_iter):
    x1 = x0 - f(x0)/df(x0)
    if abs(x1-x0)<tol:
        break
    x0=x1
print('The solution:',x1)