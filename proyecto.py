from sympy import*
from tabulate import tabulate

def preparar():
    A = "l*sin(b*0.0174532)"
    B = "l*cos(b*0.01745329252)"
    C = "((h + 0.5*D)*sin(b*0.01745329252) -0.5*D*tan(b*0.01745329252))"
    E = "((h + 0.5*D)*cos(b*0.01745329252) - 0.5*D)"

    valor_l = input("Ingrese el valor de l:\n")
    valor_b = input("Ingrese el valor de b:\n")
    valor_h = input("Ingrese el valor de h:\n")
    valor_D = input("Ingrese el valor de D:\n")

    funcion_A = sympify(A)
    funcion_B = sympify(B)
    funcion_C = sympify(C)
    funcion_E = sympify(E)

    A_evaluado = funcion_A.evalf(subs = {"l" : valor_l , "b" : valor_b})
    B_evaluado = funcion_B.evalf(subs = {"l" : valor_l , "b" : valor_b})
    C_evaluado = funcion_C.evalf(subs = {"h" : valor_h , "b" : valor_b , "D" : valor_D})
    E_evaluado = funcion_E.evalf(subs = {"h" : valor_h , "b" : valor_b , "D" : valor_h})

    A = str(A_evaluado)
    B = str(B_evaluado)
    C = str(C_evaluado)
    E = str(E_evaluado)
    return A,B,C,E

def preparar_funcion(A,B,C,E):

    funcion_def = A + "*sin(a*0.01745329252)*cos(a*0.01745329252) +" + B + "*sin(a*0.01745329252)**2 -" + C + "*cos(a*0.01745329252) -" + E + "*sin(a*0.01745329252)"
    funcion_lista = sympify(funcion_def)    #convierte el string ingresado en una expresion literal
    return funcion_lista

def Newton(funcion_lista,df,matriz):

    valor = float(input("Ingrese el valor inicial:\n"))
    print ("")
    valor_df = df.evalf(subs = {"a" : valor})   #evalua el valor ingresado en la funcion derivada
    valor_funcion = funcion_lista.evalf(subs = {"a" : valor})   #evaula el valor ingresado en la funcion
    Newton1 = valor - (float(valor_funcion) / float(valor_df))  #expresion de Newton

    for i in range(0,1):
        matriz.append([])
        for j in range(0,10):
            if (i == 0 and j ==0):
                valor_df = df.evalf(subs = {"a" : Newton1})
                valor_funcion = funcion_lista.evalf(subs = {"a" : Newton1})
                Newton1 = valor - (float(valor_funcion) / float(valor_df))
                matriz[i].append(Newton1)
                Newton2 = Newton1
            else:
                valor_df = df.evalf(subs = {"a" : Newton2})
                valor_funcion = funcion_lista.evalf(subs = {"a" : Newton2})
                Newton2 = Newton2 - (float(valor_funcion) / float(valor_df))
                matriz[i].append(Newton2)  #agrega el valor obtenido a un arreglo

    return matriz

def main():

    proyecto = "Super proyecto de Analisis numerico"
    print ("")

    print (proyecto.center(50," "))
    print ("")
    print ("Integrantes:\n")
    print ("   Byron Pucha\n   David Pazmino\n")

    nombre = "Ejercico 30"

    print (nombre.center(50," "))
    print("\n")
    matriz=[]

    A,B,C,E =  preparar()
    funcion_lista = preparar_funcion(A,B,C,E)
    df = diff(funcion_lista)    #esta funcion obtiene la derivada de la funcion en terminos de la variable
    matriz = Newton(funcion_lista,df,matriz)
    print (tabulate(matriz, headers = ["x1","x2","x3","x4","x5","x6","x7","x8","x9","x10"], tablefmt="fancy_grid"))
    print ("")
    print ("El resultado de la iteracion es:   " , matriz[0][9])

if __name__ == "__main__":
    main()
