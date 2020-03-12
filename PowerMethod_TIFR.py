'''This is a program to find the dominant eigenvector and dominant eigenvalue o a given Matrix using Power Method

Author:- Souparna Nath

Date:- 11/03/2020'''

import numpy as np

x_0 = np.array([1.,1.,1.])    #Initial Guess Dominant Eigenvector

A = np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])

def PowerMethod(n):
    x = np.dot(A,x_0)

    for i in range(1,n):
        x = np.dot(A,x)

        norm = 0.

        for i in x:
            norm += i**2

        e_vec = 1/np.sqrt(norm)*x    #Normalizing the Eigenvector

        e_val = np.vdot(np.dot(A,e_vec),e_vec)    #<AX|X> = l<X|X> = l

    return e_val,e_vec

n = 0

while(True):
    n = (int)(input("Enter no. of iterations: "))

    e_val_1 = PowerMethod(n)[0]
    e_val_2 = PowerMethod(n-1)[0]
    
    if((e_val_1 - e_val_2)/e_val_2 >= 0.001):
        print("Enter more number of iterations!")

    else:
        break

e_val_f,e_vec_f  = PowerMethod(n)

print("The dominant eigenvalue: ")
print(e_val_f)
print("The dominant eigenvector: ")
print(e_vec_f)

print(np.linalg.eigh(A))
