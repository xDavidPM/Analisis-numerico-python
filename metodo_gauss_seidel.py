from sympy import *
import numpy as np
from numpy.linalg import inv

# Metodo de gauss seidel

matrix = [[5,-1,-1],[-1,4,-1],[-1,-1,4]] # matriz de datos
B = [[10.1],[7.7],[7.4]]                     # valores contanstantes
x0 = [[0],[0],[0]]                           # valores iniciales
x1 = [[0],[0],[0]]                           # valores iniciales
r = [[0],[0],[0]]                           # valores iniciales

n = len(matrix[0])
m = len(matrix)


tj = np.zeros((m,n))

D=np.zeros((m,n))
R=np.zeros((m,n))
L=np.zeros((m,n))

for i in range(0,m):
    for j in range(0,n):
        if (j==i):
            D[j][i] = matrix[j][i]
        if (j>i):
            L[j][i] = matrix[j][i]
        if (j<i):
            R[j][i] = matrix[j][i]

ts = -(inv(D+L)).dot(R)
cs = (inv(D+L)).dot(B)

error =1
a =1
while(error>0.001):
    x0 = x1
    x1 = (ts.dot(x0)) + cs
    error = max(abs(x1 - x0))
    print (x1)
    print("")
    a+=1
print(a)

#r = B -(matrix.dot(x0))
#print(r)
