#Aim: Find the solution of transcendental equation tanx=x using Newton Raphson Method
import math

#Define the function
def f(x):
    return x-math.tan(x)
#Define tha derivative of the function
def df(x):
    return 1-(1/math.cos(x))**2
#Initial guess
x0=1.0
#Tolerance
tol=1e-6

#Maximum number of iterations 
max_iter=100

#Newton-Raphson Method
for i in range(max_iter):
    x1=x0-f(x0)/df(x0)
    if abs(x1 - x0) < tol:
        break
    x0=x1
print('The solution is:',x1)
