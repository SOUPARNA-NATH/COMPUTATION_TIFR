""" These are a series of codes on solving IVP Differential Equations 
via scipy.integrate module

Author :- Souparna Nath

Date:- 20/04/2020
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def f1(t,y):
    return t*np.exp(3*t) - 2*y

t1 = np.arange(0,1,0.01)
y0 = np.array([0])

sol = integrate.solve_ivp(f1, (0,1), y0,t_eval = t1)

t_plot = sol.t
y_approx = (sol.y).T
y_exact = 1/25*(np.exp(3*t1)*(5*t1-1)+np.exp(-2*t1))

plt.plot(t_plot,y_approx,label = r"Approximate Solution of $y' = te^{3t}-2y$")
plt.plot(t_plot,y_exact,label = r"Exact Solution $\frac{1}{25}\ e^{3t}(5t-1)+e^{-2t}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("ODE USING solve_ivp MODULE")
plt.grid(True)
plt.show()

def f2(t,y):
    return 1-(t-y)**2

t2 = np.arange(2,3,0.01)
y0 = np.array([1])

sol = integrate.solve_ivp(f2, (2,3), y0,t_eval = t2)

t_plot = sol.t
y_approx = (sol.y).T
y_exact = (t2**2 - 3*t2 + 1)/(t2-3)

plt.plot(t_plot,y_approx,label = r"Approximate Solution of $y' = 1-(t-y)^2$")
plt.plot(t_plot,y_exact,label = r"Exact Solution $\frac{t^2 - 3t + 1}{t-3}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("ODE USING solve_ivp MODULE")
plt.grid(True)
plt.show()

def f3(t,y):
    return 1 + y/t

t3 = np.arange(1,2,0.01)
y0 = np.array([2])

sol = integrate.solve_ivp(f3, (1,2), y0,t_eval = t3)

t_plot = sol.t
y_approx = (sol.y).T
y_exact = 2*t3 + t3*np.log(t3)

plt.plot(t_plot,y_approx,label = r"Approximate Solution of $y' = 1+\frac{y}{t}$")
plt.plot(t_plot,y_exact,label = r"Exact Solution $2t\ +\ t\log{t}$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("ODE USING solve_ivp MODULE")
plt.grid(True)
plt.show()

def f4(t,y):
    return np.cos(2*t) + np.sin(3*t)

t4 = np.arange(0,1,0.01)
y0 = np.array([1])

sol = integrate.solve_ivp(f4, (0,1), y0,t_eval = t4)

t_plot = sol.t
y_approx = (sol.y).T
y_exact = 1/6*(8 - 2*np.cos(3*t4) + 3*np.sin(2*t4))

plt.plot(t_plot,y_approx,label = r"Approximate Solution of $y' = \sin{2t} + \cos{3t}$")
plt.plot(t_plot,y_exact,label = r"Exact Solution $\frac{1}{6}\ (8 - 2\cos{3t} + 3\sin{2t})$")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("ODE USING solve_ivp MODULE")
plt.grid(True)
plt.show()
