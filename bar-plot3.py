import matplotlib.pyplot as plt
import numpy as np

# Sample data
labels = ['A', 'B', 'C', 'D']
group1 = [1, 4, 2, 5]
group2 = [2, 3, 5, 1]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

# Plotting the first group of bars
plt.bar(x - width/2, group1, width, color='b')

# Plotting the second group of bars
plt.bar(x + width/2, group2, width, color='r')

# Adding labels and title
plt.xlabel('Labels')
plt.ylabel('Values')
plt.title('Grouped Bar Chart Example')
plt.xticks(x, labels)

# Display plot
plt.show()
