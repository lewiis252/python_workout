import matplotlib.pyplot as plt
import numpy as np

rang = np.arange(-2, 0, 0.001)

x_coord = np.array([4-y**2 for y in rang])
y_coord = np.array([4*y for y in rang])
print(x_coord)
print(y_coord)

plt.scatter(x_coord, y_coord)
plt.show()