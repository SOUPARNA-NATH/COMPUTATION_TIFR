""" These are a series of codes on solving BVP Differential Equations 
via scipy.integrate module

Author :- Souparna Nath

Date:- 20/04/2020
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
'''
Let
y[0] be y
y[1] be z = y'
for all the subsequent cases
'''

'''
Given BV Differential equation y'' = -e^(-2y)
Splitting it into 2 1st order differential equations
y' = z
z' = -e^(-2y)
Solving these Simultaeneously would yield the result
'''

def f1(x,y):
    return np.vstack((y[1],-np.exp(-2*y[0])))

def bc1(ya,yb):
    return np.array([ya[0],yb[0] - np.log(2)])  #Boundary Conditions are the
                                                #that are sybtracted from ya[0],yb[0]

x1 = np.arange(1,2.01,0.04)
y1 = np.zeros((2,x1.size))    #assigning initial values at each mesh node

sol1 = integrate.solve_bvp(f1,bc1,x1,y1)

x_plot = sol1.x
y_approx_1 = sol1.y[0]
#y_exact_1 = 1/25*(np.exp(3*t1)*(5*t1-1)+np.exp(-2*t1))

plt.plot(x_plot,y_approx_1,label = r"Approximate Solution of $y'' = -e^{-2y}$")
#plt.plot(x_plot,y_2,label = r"Exact Solution $\frac{1}{25}\ e^{3t}(5t-1)+e^{-2t}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING solve_bvp MODULE")
plt.grid(True)
plt.show()

'''
Given BV Differential equation y'' = y'cos(x) -y*ln(y)
Splitting it into 2 1st order differential equations
y' = z
z' = z*cos(x) -y*ln(y)
Solving these Simultaeneously would yield the result
'''

def f2(x,y):
    return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))

def bc2(ya,yb):
    return np.array([ya[0] -1, yb[0]- np.exp(1)])

x2 = np.arange(0,np.pi/2 +0.01,0.04)
y2 = np.zeros((2,x2.size))
y2[0] = 2
y2[1] = 2

sol2 = integrate.solve_bvp(f2,bc2,x2,y2)

x_plot = sol2.x
y_approx_2 = sol2.y[0]
#y_exact_2 = 1/25*(np.exp(3*t1)*(5*t1-1)+np.exp(-2*t1))

plt.plot(x_plot,y_approx_2,label = r"Approximate Solution of $y'' = y'\cos{x}-y\ln{y}$")
#plt.plot(x_plot,y_2,label = r"Exact Solution $\frac{1}{25}\ e^{3t}(5t-1)+e^{-2t}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING solve_bvp MODULE")
plt.grid(True)
plt.show()

'''
Given BV Differential equation y'' = -(2(y')^3 + y^2*y')*sec(x)
Splitting it into 2 1st order differential equations
y' = z
z' = -(2*z^3 + z*y^2)*sec(x)
Solving these Simultaeneously would yield the result
'''

def f3(x,y):
    return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*(1/np.cos(x))))

def bc3(ya,yb):
    return np.array([ya[0]- 2**0.25, yb[0]- 0.5*12**0.25])

x3 = np.arange(np.pi/4,np.pi/3 +0.01,0.01)
y3 = np.zeros((2,x3.size))
y3[0] = 0
y3[1] = 0

sol3 = integrate.solve_bvp(f3,bc3,x3,y3)

x_plot = sol3.x
y_approx_3 = sol3.y[0]

#y_exact_3 = 1/25*(np.exp(3*t1)*(5*t1-1)+np.exp(-2*t1))

plt.plot(x_plot,y_approx_3,label = r"Approximate Solution of $y' = -(2(y')^3 + y^2y')\sec{x}$")

#plt.plot(x_plot,y_2,label = r"Exact Solution $\frac{1}{25}\ e^{3t}(5t-1)+e^{-2t}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING solve_bvp MODULE")
plt.grid(True)
plt.show()

'''
Given BV Differential equation y'' = 1/2 - y'^2/2 - y*sin(x)/2
Splitting it into 2 1st order differential equations
y' = z
z' = 1/2 - z^2/2 - y*sin(x)/2
Solving these Simultaeneously would yield the result
'''

def f4(x,y):
    return np.vstack((y[1], 0.5-y[1]**2/2-y[0]*np.sin(x)/2))

def bc4(ya,yb):
    return np.array([ya[0]- 2, yb[0]- 2])

x4 = np.arange(0,np.pi+0.01,0.04)
y4 = np.zeros((2,x4.size))
y4[0] = 0
y4[1] = 0

sol4 = integrate.solve_bvp(f4,bc4,x4,y4)

x_plot = sol4.x
y_approx_4 = sol4.y[0]

#y_exact_4 = 1/25*(np.exp(3*t1)*(5*t1-1)+np.exp(-2*t1))

plt.plot(x_plot,y_approx_4,label = r"Approximate Solution of $y'' = \frac{1}{2} - \frac{(y')^2}{2} - \frac{y\sin{x}}{2}$")

#plt.plot(x_plot,y_2,label = r"Exact Solution $\frac{1}{25}\ e^{3t}(5t-1)+e^{-2t}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING solve_bvp MODULE")
plt.grid(True)
plt.show()
