import matplotlib.pyplot as plt

# Data to be plotted
sizes = [15, 30, 10, 45]

# Labels for the sections of the pie chart
labels = ['apple', 'mango', 'banana', 'peaches']

# Colors for the sections of the pie chart
colors = ['red', 'blue', 'green', 'yellow']

plt.pie(sizes, labels=labels, colors=colors, startangle=0)

# plt.title('People like fruits')
plt.show()
