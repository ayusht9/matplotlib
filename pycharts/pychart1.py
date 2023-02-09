import matplotlib.pyplot as plt

# Data for the pie chart
data = [20, 10, 30, 40]
labels = ['A', 'B', 'C', 'D']

# Plot the pie chart
# plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
plt.pie(data, labels=labels)

# Add a title
plt.title('Pie Chart')

# Show the plot
plt.show()