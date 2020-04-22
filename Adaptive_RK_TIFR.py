"""This is a program to solve initial value problem using Runge Kutta Method

Author:- Souparna Nath

Date:- 19/04/20
"""
import matplotlib.pyplot as plt
import numpy as np

def f(t,y):   
    return (y**2 + y)/t

a = 1
b = 3

y0 = -2

acc = 0.0001 #Aboslute accuracy
min_step = acc #minimum step to proceed


h = 0.01    #initial step size
N = 100*(b-a)

t=[a]
y_n = [y0] 

for i in range (1,N+1):
    
    #Usual Step Size
    
    k1 = f(a+(i-1)*h,y0)
    k2 = f(a+(i-1)*h + h/2, y0+ h*k1/2)  
    k3 = f(a+(i-1)*h + h/2, y0+ h*k2/2)
    k4 = f(a+(i-1)*h + h, y0 +h*k3)
    
    ynew_usual = y0 + h/6*(k1 + 2*k2 + 2*k3 + k4)

    #Half Step Size
    
    k2 = f(a+(i-1)*h + h/4, y0+ h*k1/4)  
    k3 = f(a+(i-1)*h + h/4, y0+ h*k2/4)
    k4 = f(a+(i-1)*h + h/2, y0 +h*k3/2)
    
    ynew_half = y0 + h/12*(k1 + 2*k2 + 2*k3 + k4)
    
    #Double Step Size
    
    k2 = f(a+(i-1)*h + h, y0+ h*k1)  
    k3 = f(a+(i-1)*h + h, y0+ h*k2)
    k4 = f(a+(i-1)*h + 2*h, y0 +2*h*k3)
    
    ynew_double = y0 + h/3*(k1 + 2*k2 + 2*k3 + k4)
    t.append(a+i*h)
    
    if (abs(ynew_usual) < acc):
        if(h != min_step):
            h = min_step
        #y_n.append(ynew_usual)
        y_new = ynew_usual
    
    elif(abs(ynew_usual) > acc and abs(ynew_usual-ynew_half)/abs(ynew_usual)>acc):
        h = h/2
        #y_n.append(ynew_half)
        y_new = ynew_half
        
    elif(abs(ynew_usual) > acc and abs(ynew_usual-ynew_double)/abs(ynew_usual)<acc):
        h = 2*h
        #y_n.append(ynew_double)
        y_new = ynew_double
       
    else:
        #y_n.append(ynew_usual)
        y_new = ynew_usual
    
    y0 = y_new
    y_n.append(y_new)

t = np.array(t)   
y_approx = np.array(y_n)
y_exact = 2*t/(1-2*t)

plt.plot(t,y_approx,marker = '+', ms = 5,label = r"$y' = \frac{y^2+y}{t}$")
plt.plot(t,y_exact,label = r"Exact Solution")
plt.legend(shadow = True, framealpha = 1.0)

plt.xlabel("t")
plt.ylabel(r"{$t(t)$}")
plt.title("ODE USING ADAPTIVE STEP SIZE RK METHOD (ORDER 4)")
plt.grid(True)
plt.show()