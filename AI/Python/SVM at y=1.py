import numpy as np
import matplotlib.pyplot as plt

def svm_cost_1(x):
    return np.array([0 if _ >= 1 else -0.26*(_ - 1) for _ in x])

x = np.linspace(-3, 3)
plt.plot(x, -np.log10(1 / (1+np.exp(np.negative(x)))))
plt.plot(x, svm_cost_1(x))
plt.legend(['logistic regression cost function', 'modified SVM cost function'])
plt.show()