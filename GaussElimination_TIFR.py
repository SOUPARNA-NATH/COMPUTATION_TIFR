'''This is a program to solve a system of linear equations exactly using Gaussian Elimination

Author:- Souparna Nath

Date :- 10/03/2020'''

import numpy as np
import numpy.linalg as lin

a = [[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]]
b = [2,2,2]

A = np.array(a)
B = np.array(b)

print(lin.solve(a,b))
