from sympy import*

f = ""

print
print ("Super calculo de integrales simples con metodo del trapecio c:")
print
f = raw_input("Ingrese su funcion en terminos de x:\n") #Coje el string donde se escribe la funcino
print
funcion = sympify(f) #convierte el string en una expresion literal f(x)
a = input("Ingrese su parametro inicial:\n")
b = input("Ingrese su parametro final:\n")
m = input("Ingrese el numero de particiones\n")


def trapecios(funcion,a,b,m):
    h = (b-a)/float(m)
    s = 0
    n = 0
    a_evaluado = 0
    b_evaluado = 0

    for i in range(1,m):
        n = a + (i*h)
        n_evaluado = funcion.evalf(subs = {"x" : n}) #evalua n en la funcion descrita
        s = s + n_evaluado

    a_evaluado = funcion.evalf(subs = {"x" : a}) #evalua a en la funcion descrita, lo mismo con b en la siguiente linea
    b_evaluado = funcion.evalf(subs = {"x" : b})
    resul = h/2 * (a_evaluado + 2*s + b_evaluado)

    return resul


print trapecios(funcion,a,b,m)  #el primer parametro debe ser la funcion en expresion literal
