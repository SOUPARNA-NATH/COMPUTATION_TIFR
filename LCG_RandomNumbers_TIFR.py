'''Program to Generate Random Numbers using the method 

X_{i+1} = (a*X_{i} + c)%m

'''

import matplotlib.pyplot as plt
import numpy as np
import timeit as time

a = int(input("Enter the Multiplicative Constant: "))   #Preferably high values
c = int(input("Enter the Additive Constant: ")) #Preferably high values
m = int(input("Enter the modulus: "))   #Especially a high value
X = int(input("Enter your seed value: "))

X_i = [X]

for i in range(10000):
    X_next = (a*X_i[i] + c)%m
    X_i.append(X_next)

i = np.arange(0,10001,1)
Xi = np.array(X_i)/(m-1)

plt.xlabel("i")
plt.ylabel(r"$X_i$")
plt.title("Linear Congruential Random Numbers") 
plt.scatter(i,Xi)
plt.show()

plt.xlabel(r"$X_i$")
plt.ylabel(r"Probability $P(X_i)$")
plt.title("Probability Distribution of LCG")
plt.hist(Xi,bins = 10,density = True,color = 'r')
plt.show()

'''
uniform = np.ones(10001)
plt.title("Uniform Distribution")
plt.hist(uniform, bins = 10, density = True, color = 'r')
'''

mysetup = '''import matplotlib.pyplot as plt
import numpy as np

a = int(input("Enter the Multiplicative Constant: "))   #Preferably high values
c = int(input("Enter the Additive Constant: ")) #Preferably high values
m = int(input("Enter the modulus: "))   #Especially a high value
X = int(input("Enter your seed value: "))'''

mycode = '''X_i = [X]

for i in range(10000):
    X_next = (a*X_i[i] + c)%m
    X_i.append(X_next)

i = np.arange(0,10001,1)
Xi = np.array(X_i)/(m-1)'''

print("Time taken: ",time.timeit(stmt = mycode, setup = mysetup, number = 10000))

