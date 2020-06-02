'''Program to Generate Random Numbers using Python Module
'''

import matplotlib.pyplot as plt
import numpy as np
import timeit as time

i = np.arange(1,10001,1)
X_i = np.random.rand(10000)

plt.xlabel("i")
plt.ylabel(r"$X_i$")
plt.title("Module generated Random Numbers") 
plt.scatter(i,X_i)
plt.show()

plt.xlabel(r"$X_i$")
plt.ylabel(r"Probability $P(X_i)$")
plt.title("Probability Distribution")
plt.hist(X_i,bins = 10,density = True,color = 'r')
plt.show()


'''
uniform = np.ones(10001)
plt.title("Uniform Distribution")
plt.hist(uniform, bins = 10, density = True, color = 'r')
'''

mysetup = '''
import matplotlib.pyplot as plt
import numpy as np'''

mycode = '''i = np.arange(1,10001,1)
X_i = np.random.rand(10000)'''

print("Time Taken: ",time.timeit(stmt = mycode, setup = mysetup, number = 10000))