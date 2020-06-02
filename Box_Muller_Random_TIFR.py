'''Program to Generate Random Numbers using Box-Muller Method
'''

import matplotlib.pyplot as plt
import numpy as np

i = np.arange(1,10001,1)
X_1 = np.random.rand(10000)
X_2 = np.random.rand(10000)

Y_1 = np.sqrt(-2*np.log(X_1))*np.cos(2*np.pi*X_2)
Y_2 = np.sqrt(-2*np.log(X_1))*np.sin(2*np.pi*X_2)

plt.xlabel("i")
plt.ylabel(r"$X_i$")
plt.title("Box-Muller Random Numbers") 
plt.scatter(i,Y_1)
plt.show()

plt.xlabel(r"$X_i$")
plt.ylabel(r"Probability $P(X_i)$")
plt.title("Probability Distribution")
plt.hist(Y_1,bins = 10,density = True,color = 'r')
plt.show()

