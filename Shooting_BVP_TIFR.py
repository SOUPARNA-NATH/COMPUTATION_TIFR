"""This is a program to solve boundary value problem using Shooting Method

Author:- Souparna Nath

Date:- 19/04/20
"""

import matplotlib.pyplot as plt
import numpy as np

"""Given Differential equation y'' = -10
Splitting it into 2 1st order differential equations
y' = z
z' = -10
Solving these Simultaeneously would yield the result
"""

def f1(t,y,z):   #measures change in y
    return z

def f2(t,y,z):   #measures change in z
    return -10

a = 0
b = 10

y0 = 0
z0 = float(input("Enter a guess value of the derivative at x = 0: "))

h = 0.01
N = 100*(b-a)

acc = 1


while(True):
    y_n = [y0]
    z_n = [z0]
    d = z0
    for i in range (1,N+1):
        #k_i's are for change in y
        #l_i's are for change in z
        
        k1 = f1(a+(i-1)*h,y0,z0)
        l1 = f2(a+(i-1)*h,y0,z0)
        
        k2 = f1(a+(i-1)*h + h/2, y0+ h*k1/2, z0 + h*l1/2)
        l2 = f2(a+(i-1)*h + h/2, y0+ h*k1/2, z0 + h*l1/2)
        
        k3 = f1(a+(i-1)*h + h/2, y0+ h*k2/2, z0 + h*l2/2)
        l3 = f2(a+(i-1)*h + h/2, y0+ h*k2/2, z0 + h*l2/2)
        
        k4 = f1(a+(i-1)*h + h, y0 +h*k3, z0 + h*l3)
        l4 = f2(a+(i-1)*h + h, y0 +h*k3, z0 + h*l3)
        
        ynew = y0 + h/6*(k1 + 2*k2 + 2*k3 + k4)
        y_n.append(ynew)
        znew = z0 + h/6*(l1 + 2*l2 + 2*l3 + l4)
        
        y0 = ynew
        z0 = znew
    
    y_approx = np.array(y_n)
    t = np.arange(0,10.01,0.01)
    
    plt.plot(t,y_approx,label = r"Candidate for $x'(0)$ = "+str(d))
    
    if(y_approx[y_approx.size-1] < -acc):
        z0 = float(input("Estimate leads to value less than the one at boundary. Enter a larger choice: "))
        y0 = 0
    elif(y_approx[y_approx.size-1] > acc):
        z0 = float(input("Estimate leads to value more than the one at boundary. Enter a smaller choice: "))
        y0 = 0
    else:
        break;

y_exact = 50*t - 5*t**2
plt.plot(t,y_exact,label = r"Exact Solution $50t - 5t^2$")
plt.legend(shadow = True, framealpha = 1.0)
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("BVP SHOOTING METHOD USING RK ORDER 4")
plt.grid(True)
plt.show()