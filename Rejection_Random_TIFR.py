'''Program to Generate Random Numbers using Rejection Method
'''

import matplotlib.pyplot as plt
import numpy as np

def g(x):
    return np.exp(-x)

def p(x):
    return 1/np.sqrt(2*np.pi)*np.exp(-x*x/2)

i = np.arange(0,10,0.1)
X = np.random.rand(10000)*10
Y = np.random.rand(10000)*g(X)

Xp = X[Y < p(X)]
Yp = Y[Y < p(X)]

plt.xlabel("i")
plt.ylabel(r"$X_i$")
plt.title("Box-Muller Random Numbers")
plt.plot(i,p(i),'r-',label = 'Probability Distribution')
plt.plot(i,g(i),'k-',label = 'Covering Function')
plt.legend(shadow = True,framealpha = 1.0)
plt.scatter(Xp,Yp)
plt.show()

plt.xlabel(r"$X_i$")
plt.ylabel(r"Probability $P(X_i)$")
plt.title("Probability Distribution")
plt.plot(i,p(i),'b-',label = 'Probability Distribution')
plt.plot(i,g(i),'k-',label = 'Covering Function')
plt.legend(shadow = True,framealpha = 1.0)
plt.hist(Xp,bins = 10,density = True,color = 'r')
plt.show()

