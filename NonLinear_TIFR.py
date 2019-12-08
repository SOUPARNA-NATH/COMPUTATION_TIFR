""" This is a program to solve non-linear equations using modules in scipy

Author:- Souparna Nath

Date:- 08/12/2019
"""
import scipy.optimize as opt
import numpy as np

def f(x):
    return np.sin(np.cos(np.exp(x)))

root = opt.bisect(f,-1,1)
val = f(root)

print("The root of sin(cos(exp(x))) is ",root)
print("The value of the function at ",root," is ",val)
