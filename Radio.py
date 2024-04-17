import numpy as np
import matplotlib.pyplot as plt

# Radioactive decay constants
lambda_decay=0.693 #Example decay constant,corresponds to a  half-life of 1 unit of time

#Initial number of atoms
NO = 1000

#Time setting

t_max = 10
dt = 0.1 #Step size
steps = int(t_max/dt)

#Euler's Method
def euler(NO,lambda_decay,dt,steps):
    N = NO
    N_euler = []
    for _ in range(steps):
        N -= lambda_decay*N*dt
        N_euler.append(N)
    return N_euler

#RK2 Method
def rk2(NO,lambda_decay,dt,steps):
    N = NO
    N_rk2=[]
    for _ in range(steps):
        k1 = -lambda_decay*N
        k2 = -lambda_decay*(N+k1*dt)
        N+=0.5*dt*(k1+k2)
        N_rk2.append(N)
    return N_rk2

# RK4 Method
def rk4(NO,lambda_decay,dt,steps):
    N_rk4=[]
    N = NO
    for _ in range(steps):
        k1 = -lambda_decay*N
        k2 = -lambda_decay*(N + 0.5 * k1 * dt)
        k3 = -lambda_decay*(N + 0.5* k2 * dt)
        k4 = -lambda_decay*(N + k3 * dt)
        N += (dt/6)*(k1 + 2 * k2 + 2 * k3 + k4)
        N_rk4.append(N)
    return N_rk4

#Calculate solution
N_euler = euler(NO,lambda_decay,dt,steps)
N_rk2 = rk2(NO,lambda_decay,dt,steps)
N_rk4 = rk4(NO,lambda_decay,dt,steps)

#Plotting the results
t=np.linspace(0,t_max,steps)
plt.plot(t,N_euler,label='Euler')
plt.plot(t,N_rk2,label='RK2')
plt.plot(t,N_rk4,label="RK4")
plt.xlabel('Time')
plt.ylabel('Number of Atoms')
plt.legend()
plt.show()
