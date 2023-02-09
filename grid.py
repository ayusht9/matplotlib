import matplotlib.pyplot as plt

# Generate data
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# Create the plot
plt.plot(x, y)

# Add major grid
plt.grid(which='major', color='gray', linestyle='--', linewidth=0.5)

# Show the plot
plt.show()
