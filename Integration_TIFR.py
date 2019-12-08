"""This is a program to evaluate an integral of a function from 0 to 1, using modules from numpy and scipy

Author:- Souparna Nath

Date:- 09/12/2019"""

from numpy import *
from scipy.integrate import *

x = arange(0,1,0.001)
y = exp(x)

Itrap = trapz(y,x)  #Trapezoidal Rule of Integral

print("The integral of exp(x) from 0 to 1 is ",Itrap)

Isimps = simps(y,x) #Simpsons Rule of Integral
print("The integral of exp(x) from 0 to 1 is ",Isimps)

def func(x):
    return exp(x)

Iromb = romberg(func,0,1) #Romberg algorithm
print("The integral of exp(x) from 0 to 1 is ",Iromb)

IGQuad_5 = fixed_quad(func,0,1)  #Gaussian 5-point Quadrature
print("The integral of exp(x) from 0 to 1 is ",IGQuad_5)
