from sympy import *

a = 0
b = 1
n = int(input("Ingrese n :"))
f = input("Ingrese una funcion :") #(x^(-1/4))*sin(x)
h = (b-a)/n

fx = sympify(f)

x0 = a + 0.211324*h
x1 = a +h - x0
s = 0
for i in range(0,n):
    s = s + (fx.evalf(subs = {"x" : x0})) + (fx.evalf(subs = {"x" : x1}))
    x0 = x0 + h
    x1 = x1 +h
z = (h/2) * s

print(z)
