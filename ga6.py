import matplotlib.pyplot as plt
import numpy as np

# returns 10 evenly spaced samples from 0.1 to 2*PI
x = np.linspace(0.1, 2 * np.pi, 10)

markerline, stemlines, baseline = plt.stem(x, np.cos(x), '-.')

# setting property of baseline with color red and linewidth 2
plt.setp(baseline, color='r', linewidth=2)

plt.show()