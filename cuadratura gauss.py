from math import*
from sympy import*

f = ""

print ("Super calculo de integrales simples con el metodo de cuadratura gaussiana c:")
print
f = raw_input("INgrese su funcion en terminos de x:\n")
funcion = sympify(f)  #convierte la funcion de string a expresion literal
a = input("Ingrese su parametro inicial:\n")
b = input("Ingrese su parametro final:\n")


def cuadra_gausiana(funcion,a,b):
  t1 = -((b-a)/float(2))*(1/float(sqrt(3))) + ((b+a)/float(2))
  t2 = ((b-a)/float(2))* (1/float(sqrt(3))) + ((b+a)/float(2))
  t1_evaluado = funcion.evalf(subs = {"x" : t1})  #evalua t1 en la funcion
  print t1_evaluado
  t2_evaluado = funcion.evalf(subs = {"x" : t2})  #evalua t2 en la funcion
  print t2_evaluado
  resul = ((b-a) /float(2))*(t1_evaluado + t2_evaluado)
  return resul

print cuadra_gausiana(funcion,a,b)


