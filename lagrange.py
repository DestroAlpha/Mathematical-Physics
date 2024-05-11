def lagrange_interpolation(x,y,x_val):
    n = len(x)
    result=0.0
    for i in range(n):
        term=y[i]
        for j in range(n):
            if j != i:
                term *= (x_val-x[j])/(x[i]-x[j])
                result+=term
        return result
    
x=[1,2,3,4]
y=[2,3,5,8]

x_val=2.5
result=lagrange_interpolation(x,y,x_val)
print("Interpolated value at x ",x_val,"is y ",result)