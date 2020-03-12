'''This is a program to solve a system of linear equations using the various algorithms and check the speed of each

Author:- Souparna Nath

Date:- 11/03/2020'''

import numpy as np

A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])

B = np.array([1,2,3,4,5])

# Jacobi Method

x0 = np.array([0,0,0,0,0]) #Initial vector
xf = np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163]) #Analytic solution
count = 1

def Jacobi(V):
    x = []
    for i in range(5):
        s = 0
        for j in range(5):
            if(j!=i):
                s += A[i][j]*V[j]
        x.append((B[i]-s)/A[i][i])
    return np.array(x)

V = Jacobi(x0)

while(True):
    if (max(abs(xf - V)) >= 0.01): #The Maximum Difference of true and approx soln. has not yet hit 0.01 or less
        count += 1
        V = Jacobi(V)
    else:
        break

print("The approximate soln. accuarate upto 2 decimal place: ")
print(V)
print()
print("No. of iterations needed to acheieve this accuracy: ")
print(count)
print()

# Gauss Seidel Method

count = 1 #Reinitalizing Count

def GaussSeidel(V):
    x = []
    for i in range(5):
        s = 0
        for j in range(5):
            if(j<i):
                s += A[i][j]*x[j] #Using the newly modified values of our previous vector
            elif(j>i):
                s += A[i][j]*V[j] #Using the old values of the previous vector as they are not assigned yet
        x.append((B[i]-s)/A[i][i])
    return np.array(x)

V = GaussSeidel(x0)

while(True):
    if (max(abs(xf - V)) >= 0.01):
        count += 1
        V = GaussSeidel(V)
    else:
        break

print("The approximate soln. accuarate upto 2 decimal place: ")
print(V)
print()
print("No. of iterations needed to acheieve this accuracy: ")
print(count)
print()

#Conjugate Gradient Method

count = 1

V = x0 
r = B - np.dot(A,x0)
r1 = r #r1 stores the initial value of r

while(True):
    alpha = np.dot(r.T,r)/np.dot(np.dot(r1.T,A),r1)
    V = V + alpha*r1
    r2 = r
    r = r - np.dot(alpha*A,r1)
    if (np.all(abs(xf - V) <= 0.01)):
        break
    else:
        beta = (np.dot(r.T,r))/np.dot(r2.T,r2)
        r1 = r + beta*r1
        count += 1

print("The approximate soln. accuarate upto 2 decimal place: ")
print(V)
print()
print("No of iterations to achieve this accuracy: ")
print(count)
print()
