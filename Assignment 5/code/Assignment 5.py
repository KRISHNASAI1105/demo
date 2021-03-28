import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

k = 1
x = np.linspace(0, 50, 100, endpoint = False)
y = (k - np.exp(-x))

plt.plot(x, y, '-b', label = '$y = 1 - e^{-x}$')

axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])

plt.xlabel('X')
plt.ylabel('F(x)')
plt.title('CDF of X')
plt.legend(loc='upper left')

plt.show()

x = np.linspace(0, 50, 100, endpoint = False)
y = (np.exp(-x))

plt.plot(x, y, '-b', label = '$y = e^{-x}$')

axes = plt.gca()
axes.set_xlim([x.min(), x.max()])
axes.set_ylim([y.min(), y.max()])

plt.xlabel('x')
plt.ylabel('F′(x)')
plt.title('Probability')
plt.legend(loc='upper left')

plt.show()