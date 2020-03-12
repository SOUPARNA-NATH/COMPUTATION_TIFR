'''This is to code a program to perform a singular value decomposition of the given matrix and to verify the decomposition using linalg module

Author:- Souparna Nath

Date:- 11/03/2020'''

import numpy as np

A = np.array(([0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]))

U_evec = np.linalg.eigh(np.dot(A,A.T))[1] #The matrix of eigenvectors of A.Trn(A) is U 

V_evec = np.linalg.eigh(np.dot(A.T,A))[1] #The matrix of eigenvectors of Trn(A).A is V

S = np.dot(np.dot(U_evec.T,A),V_evec) #The decomposition of A into U.S.Trn(V) implies S = Trn(U).A.V

print("The singular value decompostion: ")
print()
print("U = ",U_evec)
print()
print("S = ",S)
print()
print("V = ",V_evec)

print()
print("The singular value decomposition using module: ")
print()
u,s,v = np.linalg.svd(A)
print("U = ",u)
print()
print("S = ",s)
print()
print("V = ",v)
