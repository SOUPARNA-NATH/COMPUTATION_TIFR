""" This is a program to solve non-linear equations using modules in scipy

Author:- Souparna Nath

Date:- 08/12/2019
"""
import scipy.optimize as opt
import numpy as np

def f(x):
    return np.sin(np.cos(np.exp(x)))

def fprime(x):
    return -np.exp(x)*np.sin(np.exp(x))*np.cos(np.cos(np.exp(x)))

root = opt.newton(f,-0.1,fprime)
val = f(root)

print("The root of sin(cos(exp(x))) is ",root)

print("The value of the function at ",root," is ",val)

print("The value of f\'(x) at -1 is",fprime(-1))
print("The value of f\'(x) at -0.1 is",fprime(-0.1))

