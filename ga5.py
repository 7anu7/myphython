import matplotlib.pyplot as plt
import numpy as np
...
x = np.random.rand(100,1)

plt.ylabel('Relative Cumulative Frequency')
plt.xlabel('Normalized Eigenvalues')

binsCnt = 50
bins = np.append(np.linspace(x.min(), x.max(), binsCnt), [np.inf])
plt.hist(x, bins = bins, normed=1, histtype='step', cumulative=True)
# Limit X and Y ranges
plt.xlim(0, 2)
plt.ylim(0, 1)
plt.show()