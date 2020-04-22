"""This is a program to solve initial value problem using Runge Kutta Method

Author:- Souparna Nath

Date:- 19/04/20
"""

import matplotlib.pyplot as plt
import numpy as np

"""Given System of Differential equations
 u1' = u1 + 2*u2 - 2*u3 + e^-t
 u2' = u2 + u3 - 2*e^-t
 u3' = u1 + 2*u2 + e^-t 
Solving these Simultaeneously would yield the result
"""

def f1(t,u1,u2,u3):   #measures change in u1
    return u1 + 2*u2 - 2*u3 + np.exp(-t)

def f2(t,u1,u2,u3):   #measures change in u2
    return u2 + u3 - 2*np.exp(-t)

def f3(t,u1,u2,u3): #measures change in u3
    return u1 + 2*u2 + np.exp(-t)

a = 0
b = 1

u1_0 = 3
u2_0 = -1
u3_0 = 1

h = 0.01
N = 100*(b-a)

u1_n = [u1_0]
u2_n = [u2_0]
u3_n = [u3_0]

for i in range (1,N+1):
    #k_i's are for change in u1
    #l_i's are for change in u2
    #m_i's are for change in u3
    
    k1 = f1(a+(i-1)*h,u1_0,u2_0,u3_0)
    l1 = f2(a+(i-1)*h,u1_0,u2_0,u3_0)
    m1 = f3(a+(i-1)*h,u1_0,u2_0,u3_0)
    
    k2 = f1(a+(i-1)*h + h/2, u1_0+ h*k1/2, u2_0 + h*l1/2, u3_0 + h*m1/2)
    l2 = f2(a+(i-1)*h + h/2, u1_0+ h*k1/2, u2_0 + h*l1/2, u3_0 + h*m1/2)
    m2 = f3(a+(i-1)*h + h/2, u1_0+ h*k1/2, u2_0 + h*l1/2, u3_0 + h*m1/2)
    
    k3 = f1(a+(i-1)*h + h/2, u1_0+ h*k2/2, u2_0 + h*l2/2, u3_0 + h*m2/2)
    l3 = f2(a+(i-1)*h + h/2, u1_0+ h*k2/2, u2_0 + h*l2/2, u3_0 + h*m2/2)
    m3 = f3(a+(i-1)*h + h/2, u1_0+ h*k2/2, u2_0 + h*l2/2, u3_0 + h*m2/2)
    
    k4 = f1(a+(i-1)*h + h, u1_0 +h*k3, u2_0 + h*l3, u3_0 + h*m3)
    l4 = f2(a+(i-1)*h + h, u1_0 +h*k3, u2_0 + h*l3, u3_0 + h*m3)
    m4 = f3(a+(i-1)*h + h, u1_0 +h*k3, u2_0 + h*l3, u3_0 + h*m3)
    
    u1_new = u1_0 + h/6*(k1 + 2*k2 + 2*k3 + k4)
    u1_n.append(u1_new)
    u2_new = u2_0 + h/6*(l1 + 2*l2 + 2*l3 + l4)
    u2_n.append(u2_new)
    u3_new = u3_0 + h/6*(m1 + 2*m2 + 2*m3 + m4)
    u3_n.append(u3_new)
    
    u1_0 = u1_new
    u2_0 = u2_new
    u3_0 = u3_new
    
u1_approx = np.array(u1_n)
u2_approx = np.array(u2_n)
u3_approx = np.array(u3_n)

t = np.arange(0,1.01,0.01)

plt.plot(t,u1_approx,label = r"$u_1$(t)")
plt.plot(t,u2_approx,label = r"$u_2$(t)")
plt.plot(t,u3_approx,label = r"$u_3$(t)")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel(r"{$u_1(t),u_2(t),u_3(t)$}")
plt.title("ODE USING RUNGE KUTTA METHOD (ORDER 4)")
plt.grid(True)
plt.show()