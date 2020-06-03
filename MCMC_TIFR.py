import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

def p(theta):
    if (3.0 < theta < 7.0):
        return theta
    else:
        return 0.0

X_1 = np.random.rand(5000)
X_2 = np.random.rand(5000)

Y_1 = np.sqrt(-2*np.log(X_1))*np.cos(2*np.pi*X_2)
Y_2 = np.sqrt(-2*np.log(X_1))*np.sin(2*np.pi*X_2)

theta = 5
Y = []
step = np.arange(0,5000,1)

for i in step:
    theta_p = theta + Y_1[i]
    r = np.random.rand()
        
    if(p(theta_p)/p(theta) > r):
        theta = theta_p
        
    Y.append(theta)
    
plt.xlabel("step")
plt.ylabel(r"$\theta$")
plt.title("Markov Chain")
plt.plot(step,Y,'b-',marker = "o",ms = 2.5,mfc = 'r', mec = 'r')
plt.show()

plt.xlabel(r"p($\theta$)")
plt.ylabel(r"$\theta$")
plt.title("Probability Distribution")
plt.hist(Y,bins = 10,density = True,color = 'r')
plt.show()
