"""This is a program to solve initial value problem using Euler's Backward Method

Author:- Souparna Nath

Date:- 19/04/20
"""
import matplotlib.pyplot as plt
import numpy as np

#Solving dy/dx = -9y

def f1(x,y):
    return -9*y

a = 0
b = 1
y0 = np.e

N = 100*(b-a)

y_n = [y0]

for i in range(1,N+1):
    """
    y1 = y0 + h*f(x1,y1)
    Implies y1 = y0 + h*f(x0+h, y0 + h*f(x0,y0))
    Similarly for others
    """
    ynew = y0 + 0.01*f1(a+i*0.01,y0 + 0.01*f1(a+(i-1)*0.01,y0))
    y_n.append(ynew)
    y0 = ynew

y_approx = np.array(y_n)

x = np.arange(0,1.01,0.01)
y_exact = np.exp(-9*x+1)

abs_err = np.abs(y_exact - y_approx)
rel_err = abs_err/y_exact

plt.plot(x,y_approx,label = r"Approximate Solution of $\ \frac{dy}{dx}$ = -9y")
plt.plot(x,y_exact,label = r"Exact Solution y = $e^{9x-1}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING BACKWARD EULER'S METHOD")
plt.grid(True)
plt.show()

plt.plot(x,abs_err,label = "Absolute error")
plt.plot(x,rel_err,label = "Relative Error")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("Error(x)")
plt.title("ERROR USING BACKWARD EULER'S METHOD")
plt.grid(True)
plt.show()

# dy/dx = -20(y-x)^2 +2x

def f2(x,y):
    return (-20*(y-x)**2 + 2*x)

a = 0
b = 1
y0 = 1/3

N = 100*(b-a)

y_n = [y0]

for i in range(1,N+1):
    """
    y1 = y0 + h*f(x1,y1)
    Implies y1 = y0 + h*f(x0+h, y0 + h*f(x0,y0))
    Similarly for others
    """
    ynew = y0 + 0.01*f2(a+i*0.01,y0 + 0.01*f2(a+(i-1)*0.01,y0))
    y_n.append(ynew)
    y0 = ynew

y_approx = np.array(y_n)

x = np.arange(0,1.01,0.01)

plt.plot(x,y_approx,label = r"Approximate Solution of $\ \frac{dy}{dx} = -20(y-x)^2 + 2x$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("ODE USING BACKWARD EULER'S METHOD")
plt.grid(True)
plt.show()