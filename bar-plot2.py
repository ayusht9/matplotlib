import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
values1 = [1, 4, 2, 5]
values2 = [2, 3, 5, 1]

# Plotting the first bar plot
plt.bar(labels, values1, color='b')

# Plotting the second bar plot
plt.bar(labels, values2, color='r', bottom=values1)

# Adding labels and title
plt.xlabel('Labels')
plt.ylabel('Values')
plt.title('Double Bar Plot Example')

# Display plot
plt.show()
