'''Program to Generate Random Numbers using Rejection Method
'''

import matplotlib.pyplot as plt
import numpy as np

count = 0
X = np.random.rand(100000)
Y = np.random.rand(100000)

for i in range(100000):
    if((X[i])**2 + (Y[i])**2 <= 1):
        count += 1

Area  = 4*count/100000

print("Area of the circle", Area)

count = 0

X1 = np.random.rand(100000)
X2 = np.random.rand(100000)
X3 = np.random.rand(100000)
X4 = np.random.rand(100000)
X5 = np.random.rand(100000)
X6 = np.random.rand(100000)
X7 = np.random.rand(100000)
X8 = np.random.rand(100000)
X9 = np.random.rand(100000)
X10 = np.random.rand(100000)

for i in range(100000):
    if(X1[i]**2 + X2[i]**2 + X3[i]**2 + X4[i]**2 + X5[i]**2 + X6[i]**2 + X7[i]**2 +X8[i]**2 + X9[i]**2 + X10[i]**2 <= 1):
        count += 1

Vol  = (2**10)*count/100000

print("Volume of 10D Volume of Sphere",Vol)