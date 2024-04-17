import numpy as np
import matplotlib.pyplot as plt

def dIdt(t, I, R, L, V):
    # Define the differential equation for RL circuit
    return (V - I * R) / L

def runge_kutta_4th_order(t0, I0, t, h, R, L, V):
    n = int((t - t0) / h)
    I = I0
    I_values = [I0]

    for _ in range(n):
        k1 = h * dIdt(t0, I, R, L, V)
        k2 = h * dIdt(t0 + 0.5 * h, I + 0.5 * k1, R, L, V)
        k3 = h * dIdt(t0 + 0.5 * h, I + 0.5 * k2, R, L, V)
        k4 = h * dIdt(t0 + h, I + k3, R, L, V)
        I = I + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t0 += h
        I_values.append(I)

    return I_values

# Example usage
t0, I0, t, h = 0, 0, 2, 0.001
R = 10  # Resistance (ohms)
L = 0.5  # Inductance (henrys)
V = 5  # DC voltage (volts)

current_values = runge_kutta_4th_order(t0, I0, t, h, R, L, V)

# Plot the current vs. time
time_values = np.arange(t0, t + h, h)
plt.plot(time_values, current_values)
plt.xlabel("Time (s)")
plt.ylabel("Current (A)")
plt.title("Current in RL Circuit")
plt.grid(True)
plt.show()
