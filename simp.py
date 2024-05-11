def simpsons_rule(f, a, b, n):
    """
    Compute the definite integral of f from a to b using Simpson's rule.

    Parameters:
        f (function): The integrand function.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of intervals (must be even).

    Returns:
        float: The approximate value of the definite integral.
    """
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even.")

    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3

    return integral

# Example usage:
def integrand(x):
    return x**2

a = 0
b = 1
n = 10  # Number of intervals (must be even)
integral = simpsons_rule(integrand, a, b, n)
print("Approximate integral:", integral)
