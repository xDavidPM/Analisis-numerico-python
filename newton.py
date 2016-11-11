from sympy import*
from tabulate import tabulate

def Newton(fx,derivada_fx,matriz):

    valor = input("Ingrese el valor inicial:\n")
    print ("")
    valor_df = derivada_fx.evalf(subs = {"x" : valor})   #evalua el valor ingresado en la funcion derivada
    valor_funcion = fx.evalf(subs = {"x" : valor})   #evaula el valor ingresado en la funcion
    Newton1 = valor - (float(valor_funcion) / float(valor_df))  #expresion de Newton

    for i in range(0,1):
        matriz.append([])
        for j in range(0,10):
            if (i == 0 and j ==0):
                valor_df = derivada_fx.evalf(subs = {"x" : Newton1})
                valor_funcion = fx.evalf(subs = {"x" : Newton1})
                Newton1 = valor - (float(valor_funcion) / float(valor_df))
                matriz[i].append(Newton1)
                Newton2 = Newton1
            else:
                valor_df = derivada_fx.evalf(subs = {"x" : Newton2})
                valor_funcion = fx.evalf(subs = {"x" : Newton2})
                Newton2 = Newton2 - (float(valor_funcion) / float(valor_df))
                matriz[i].append(Newton2)  #agrega el valor obtenido a un arreglo

    return matriz



def main():

    print ("\nMetodo de Newton\n")
    f = raw_input("Ingrese la funcion:\n")

    fx = sympify(f)
    derivada_fx = diff(fx)
    matriz = []

    matriz = Newton(fx,derivada_fx,matriz)
    En9 = ln(matriz[0][9])
    En8 = ln(matriz[0][8])
    En0 = ln(matriz[0][0])
    En1 = ln(matriz[0][1])
    print (tabulate(matriz, headers = ["x1","x2","x3","x4","x5","x6","x7","x8","x9","x10"], tablefmt="fancy_grid"))

    print("")
    print("la mejor aproximacion es:  ",matriz[0][9])
    print("")
    m = (En9 - En1)/(En8 - En0)
    print("la pendiente de la curva de convergencia es: ",m)

if __name__ == "__main__":
	main()
