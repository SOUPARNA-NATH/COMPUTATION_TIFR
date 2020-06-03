import matplotlib.pyplot as plt
import numpy as np

i = np.arange(1,10001,1)
X = np.random.rand(10000)
Y = -np.log(X)

plt.xlabel("i")
plt.ylabel(r"$X_i$")
plt.title("Transformed Random Numbers")
plt.scatter(i,Y)
plt.show()

plt.xlabel(r"$X_i$")
plt.ylabel(r"Probability $P(X_i)$")
plt.title("Probability Distribution")
plt.hist(Y,bins = 10,density = True,color = 'r')
plt.show()

