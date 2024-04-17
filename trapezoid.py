import math
#Define the function 
def f(x):
    return math.log(x)
#Define the interval of integration
a=2#lower limit
b=8#Upper limit

#Define the number of subintervals
n=10

#Calculate the width of each subinterval
dx=(b-a)/n
#Create a list of x values
x=[a+i*dx for i in range(n+1)]

#Initialize the sum
area=0
#Loop over each subinterval
for i in range(n):
    #Calculate the area of the trapezoid on this subinterval
    area+=(f(x[i])+f(x[i+1])/2*dx)

print(f"The approximate area under the curve is {area:.4f}")