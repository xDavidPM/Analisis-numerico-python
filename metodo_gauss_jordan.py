from sympy import *
import numpy as np
from numpy.linalg import inv

# Metodo de gauss jordan

matrix = [[45,-25,0],[-25,29,-4],[0,-4,37]] # matriz de datos
B = [[100],[100],[250]]                     # valores contanstantes
x0 = [[0],[0],[0]]                           # valores iniciales
x1 = [[0],[0],[0]]                           # valores iniciales

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

D_inv = inv(D)
tj =-D_inv.dot(L+R)
cj = D_inv.dot(B)

error =1
a =0
while(error>0.001):
    x0 = x1
    x1 = (tj.dot(x0)) + cj
    error = max(abs(x1 - x0))
    print (x1)
    print("")
    a+=1
print(a)
