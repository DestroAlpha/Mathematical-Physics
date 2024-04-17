import numpy as np
import matplotlib.pyplot as plt

#Constants 
acceleration=9.8
time_intervals=np.linspace(0,10,num=100)
dt= time_intervals[1]- time_intervals[0]

velocity=np.zeros_like(time_intervals)
position=np.zeros_like(time_intervals)

for i in range(1,len(time_intervals)):
    velocity[i]=position[i-1]+acceleration*dt
    position[i]=position[i-1]+velocity[i-1]*dt

plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.plot(time_intervals,velocity,"b-", label="Velocity(m/s)")
plt.title("Velocity vs Time")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.legend()
plt.tight_layout()
plt.show()