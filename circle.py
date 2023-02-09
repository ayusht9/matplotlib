import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10, 100)
y1=25-(x**2)
y=y1**0.5
plt.plot(x,y)

plt.show()