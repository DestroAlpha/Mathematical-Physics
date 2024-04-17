import matplotlib.pyplot as plt


# Generate some sample data (replace with your actual data)
x = (80,85,90,95,100,105,110,115,120,125)
y = (240,250,260,270,280,290,300,310,320,33)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=2, color='blue', linestyle='-.')
plt.title("Random DataSet")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

# Show the plot
plt.show()
