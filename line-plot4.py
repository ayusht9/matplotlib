import matplotlib.pyplot as plt
import numpy as np
import math

# Create some data to plot
x = np.linspace(0, 10, 100)
ph=math.radians(90)

y1 = np.sin(x)
y2 = np.sin(x+ph)
y3 = np.sin(x-ph)

plt.plot(x,y1,color='red',linestyle='--')
plt.plot(x,y2,color='green',linestyle='-')
plt.plot(x,y3,color='blue',linestyle=':')

plt.show()