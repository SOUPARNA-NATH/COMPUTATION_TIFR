"""This is a program to solve initial value problem using Runge Kutta Method

Author:- Souparna Nath

Date:- 19/04/20
"""

import matplotlib.pyplot as plt
import numpy as np

"""Given Differential equation dx/dt = 1/(x^2 + t^2)
Domain of t is from 0 to infinity
Hence Need to rescale the problem.
t = tan(z)
This sets the domain of z from 0 to pi/2
And, the differential equation becomes dx/dz = sec^2(z)/(x^2+tan(z)^2)
Solving this differential equation would yield the desired result
"""

def f(z,x):
    return  1/((np.cos(z))**2*(x**2 + (np.tan(z))**2))

a = 0
b = np.pi/2
x0 = 1

'''
In order to find the step size, we must take into account the desired
precision needed to evaluate the solution as large a value as 3.5*10**6
'''

h = np.pi/2 - np.arctan(3.5*10**6)
#h = 0.01
N = (b-a)/h

x_n = [x0]

i = 0
while (i <= (b-a)):
    
    k1 = f(a+i,x0)
    
    k2 = f(a+i + h/2, x0+ h*k1/2)
    
    k3 = f(a+i + h/2, x0+ h*k2/2,)
    
    k4 = f(a+i + h, x0 +h*k3)
    
    xnew = x0 +h/6*(k1 + 2*k2 + 2*k3 + k4)
    x_n.append(xnew)
    
    x0 = xnew
    
    i += h
x_approx = np.array(x_n)
z = np.arange(0,np.pi/2+h,h)

print("The desired value of the solution at t = 3.5*10**6 is: ")
print(x_approx[x_approx.size-2])    #last value would be that due to t = 3.5*10**6

plt.plot(z,x_approx,label = r"Approximate Solution of $\frac{dx}{dz} = \frac{\sec^2{z}}{x^2+\tan^2{z}}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("z")
plt.ylabel("x(z)")
plt.title("ODE USING RUNGE KUTTA METHOD (ORDER 4)")
plt.grid(True)
plt.show()

'''The desired value of the solution at t = 3.5*10**6 is: 
2.144818713408147
'''
