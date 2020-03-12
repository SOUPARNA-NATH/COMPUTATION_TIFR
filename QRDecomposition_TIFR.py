'''This is a progtam to find the QR Decomposition of a matrices using linalg package and subsequently to find out the eigenvalues of the matrix

Author:- Souparna Nath

Date:- 11/03/2020
'''

import numpy as np

a = [[5,-2],[-2,8]]

A_1 = np.array(a)
q,r = np.linalg.qr(A_1)
A_k = np.dot(r,q)
Q = q

for i in range(2,50):
    q,r = np.linalg.qr(A_k)
    A_k = np.dot(r,q)
    Q = np.dot(Q,q)
    
print("The diagonalised version of given matrix:- ")
print(A_k)
print("The matrix with eigenvectors as column:-")
print(Q)

print("The eigenvalues and eigenvectors using eigh module:")
e_val,e_vec = np.linalg.eigh(A_1)
print(e_val)
print(e_vec)
