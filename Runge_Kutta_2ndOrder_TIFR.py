"""This is a program to solve initial value problem using Runge Kutta Method

Author:- Souparna Nath

Date:- 19/04/20
"""

import matplotlib.pyplot as plt
import numpy as np

"""Given Differential equation y''- 2y'+y = xe^x-x
Splitting it into 2 1st order differential equations
y' = z
z' = xe^x -x-y+2z
Solving these Simultaeneously would yield the result
"""

def f(x,y,z):   #measures increment in y
    return z

def g(x,y,z):   #measures increment in z
    return x*np.exp(x)-x-y+2*z

a = 0
b = 1
y0 = 0
z0 = 0 #z0 = dy/dx at x = a = 0

h = 0.01
N = 100*(b-a)

y_n = [y0]

for i in range (1,N+1):
    #k_i's are for increment in y
    #l_i's are for increment in z
    
    k1 = f(a+(i-1)*h,y0,z0)
    l1 = g(a+(i-1)*h,y0,z0)
    
    k2 = f(a+(i-1)*h + h/2, y0+ h*k1/2, z0 + h*l1/2)
    l2 = g(a+(i-1)*h + h/2, y0+ h*k1/2, z0 + h*l1/2)
    
    k3 = f(a+(i-1)*h + h/2, y0+ h*k2/2, z0 + h*l2/2)
    l3 = g(a+(i-1)*h + h/2, y0+ h*k2/2, z0 + h*l2/2)
    
    k4 = f(a+(i-1)*h + h, y0 +h*k3, z0 + h*l3)
    l4 = g(a+(i-1)*h + h, y0 +h*k3 ,z0 +h*l3)
    
    ynew = y0 + h/6*(k1 + 2*k2 + 2*k3 + k4)
    y_n.append(ynew)
    
    znew = z0 + h/6*(l1 + 2*l2 + 2*l3 + l4)
    y0 = ynew
    z0 = znew
    
y_approx = np.array(y_n)

x = np.arange(0,1.01,0.01)
y_exact = (x**3/6-x+2)*np.exp(x)-(x+2)

plt.plot(x,y_approx,label = r"Approximate Solution of $y^{''}-2y^{'}+y = xe^x-x$")
plt.plot(x,y_exact,label = r"Exact Solution $y = \left(\frac{x^3}{6}-x+2\right)e^x-(x+2)$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING RUNGE KUTTA METHOD (ORDER 4)")
plt.grid(True)
plt.show()