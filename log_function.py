import numpy as np
import matplotlib.pyplot as plt

in_arrays=[1,1.2,1.4,1.6,1.8,2]
out_array=np.log(in_arrays)

print("Out_array: ",out_array)

plt.plot(in_arrays,in_arrays,color='blue',marker="*")

plt.plot(out_array,in_arrays,color="red",marker="o")

plt.title("Numpy.log()")
plt.xlabel("Out_array")
plt.ylabel("In_array")
plt.show()