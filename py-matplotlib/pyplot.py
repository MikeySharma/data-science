import matplotlib.pyplot as plt
import numpy as np

x = np.array([100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150])
y = np.array([500, 505, 510, 515, 520, 525, 530, 535, 540, 545, 550])

plt.plot(x, y, marker = 'x', ms = 15, linewidth=0.5, color="red")
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Trial of making a graph', fontweight="bold")
plt.grid(color = "yellow")
plt.show()
