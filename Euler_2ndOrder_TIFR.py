"""This is a program to solve initial value problem using Euler's Method

Author:- Souparna Nath

Date:- 19/04/20
"""
import matplotlib.pyplot as plt
import numpy as np

"""Given Differential equation t^2*y''- 2t*y'+ 2y = t^3*ln(t)
Splitting it into 2 1st order differential equations
y' = z
z' = 2/t*z - 2/t^2*y + t*ln(t)
Solving these Simultaeneously would yield the result
"""

def f(t,y,z):   #measures chnage in y
    return z

def g(t,y,z):   #measures change in z
    return (2/t)*z - (2/t**2)*y + t*np.log(t)

a = 1
b = 2
y0 = 1
z0 = 0 #z0 = dy/dx at x = a = 0

N = 1000*(b-a)

y_n = [y0]

for i in range(1,N+1):
    ynew = y0 + 0.001*f(a+(i-1)*0.001,y0,z0)
    y_n.append(ynew)
    
    znew = z0 + 0.001*g(a+(i-1)*0.001,y0,z0)
    y0 = ynew
    z0 = znew

y_approx = np.array(y_n)

t = np.arange(1,2.001,0.001)
y_exact = (7/4)*t + (1/2)*t**3*np.log(t) - (3/4)*t**3

abs_err = np.abs(y_exact - y_approx)
rel_err = abs_err/y_exact

plt.plot(t,y_approx,label = r"Approximate Solution of $\ t^2 y'' - 2ty'+ 2y = t^3\ln{t}$")
plt.plot(t,y_exact,label = "Exact Solution")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("ODE USING EULER'S METHOD")
plt.grid(True)
plt.show()

plt.plot(t,abs_err,label = "Absolute error")
plt.plot(t,rel_err,label = "Relative Error")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel("Error(t)")
plt.title("ERROR USING EULER'S METHOD")
plt.grid(True)
plt.show()