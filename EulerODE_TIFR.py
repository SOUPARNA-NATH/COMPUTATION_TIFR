"""This is a program to solve initial value problem using Euler's Method

Author:- Souparna Nath

Date:- 19/04/20
"""
import matplotlib.pyplot as plt
import numpy as np

def f(t,y):
    return y/t - (y/t)**2

a = 1
b = 2
y0 = 1

N = 10*(b-a)

y_n = [y0]

for i in range(1,N+1):
    ynew = y0 + 0.1*f(a+(i-1)*0.1,y0)
    y_n.append(ynew)
    y0 = ynew

y_approx = np.array(y_n)

t = np.arange(1,2.1,0.1)
y_exact = t/(1+np.log(t))

abs_err = np.abs(y_exact - y_approx)
rel_err = abs_err/y_exact

plt.plot(t,y_approx,label = r"Approximate Solution of $y' = \frac{y}{t} - \left(\frac{y}{t}\right)^2$")
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