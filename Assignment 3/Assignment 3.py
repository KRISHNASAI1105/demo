import numpy as np
from scipy.stats import bernoulli
import seaborn as sns
import matplotlib.pyplot as plt

count = 0
z = int(input("\n Enter the minimum number of resistors to be defective : "))
for i in range(0, z):
    bern_data = bernoulli.rvs(size=50, p=0.02)
    i = np.nonzero(bern_data == 1)
    defective = np.size(i)
    if defective >= 2:
        count += 1

print("\n The required probability is : ",count/z)

x=["No.of defective resistors"]
y=[count]
sns.barplot(x,y)
plt.show()