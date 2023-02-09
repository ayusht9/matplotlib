import matplotlib.pyplot as plt

# Sample data
x = ['A', 'B', 'C', 'D']
y = [1, 4, 2, 5]

# Plotting the bar plot
plt.bar(x, y)

# Adding labels and title
plt.xlabel('Hotel')
plt.ylabel('Ratings')
plt.title('Top Hotels nearby')

# Display plot
plt.show()
