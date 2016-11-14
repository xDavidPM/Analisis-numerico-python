#Super programa de Lagrange, simple y como si fuera poco multiple
def main():
    prueba = True
    while (prueba):
        print("LAGRANGE")
        print("seleccion (1) si desea usar Lagrange simple")
        print("seleccion (2) si desea usar Lagrange multiple:")
        opcion = int(input(""))
        if (opcion == 1 or  opcion == 2):
            prueba = False

    if (opcion ==1):
        x=[]
        f=[]
        valor= 0
        x,f,valor = Preparar_lagrange_simple()
        print
        print ("Su valor buscado es:")
        print (Lagrange(x,f,valor))

    if (opcion == 2):
        x = []
        y = []
        f = [[]]
        valor1 = 0
        valor2 = 0
        x,y,f,valor1,valor2 = Preparar_lagrange_multiple()
        print
        print ("Su valor buscado de su interpolacion multiple es:")
        print (Lagrange_multiple(x,y,f,valor1,valor2))


def Lagrange(x,f,v):                        #Evaluar Lagrange
    pol = 0
    for i in range(0,len(x)):
        L = 1
        for j in range(0,len(f)):
            if (i != j):
                L = L*( (v-x[j]) /float(x[i] - x[j]))
        pol = pol + L*f[i]
    return pol

def Lagrange_multiple(x,y,f,valor1,valor2):
    resul = []
    pol = 0
    for i in range(0, len(y)):
        r = 0
        parte=[]
        for j in range(0,len(x)):
            parte.append(f[j][i])
        r = Lagrange(x,parte,valor1)
        resul.append(r)
    pol = Lagrange(y,resul,valor2)
    return pol

def Preparar_lagrange_multiple():
    print ("Interpolacion de Lagrange multiple")
    print
    x = []
    y = []
    f = [[]]
    valor1 = 0
    valor2 = 0

    x = input("Ingrese los valores correspondientes de X separados por una coma:\n")
    y = input("Ingrese los valores correspondientes de Y separados por una coma:\n")
    f = input("Ingrese la matriz de variables dependientes, separandolos por parentesis y comas ejemplo: (3,4,5,8,7),(4,5,6,7),(5,6,7,8) continue :\n")
    valor1 = input("Ingrese el valor de interpolacion en X:\n")
    valor2 = input("Ingrese el valor de interpolacion en Y:\n")

    return x, y, f, valor1, valor2

def Preparar_lagrange_simple():
    print ("Interpolacion de Lagrange simple")
    print
    x=[]
    f=[]
    valor = 0

    x = input("Ingrese sus valores de X separados por comas:")
    print
    f = input("Ingrese sus valores de su funcion f(x) separados por comas:")
    print
    valor = input("Ingrese su valor a interpolar: \n")
    return x, f, valor

if __name__ == "__main__":
    main()

"""
def denominador(x,f):
    deno = []
    n = len(x)
    for i in range(0,n):
        den_parcial = 1
        for j in range(0,n):
            if (j != i):
                den_parcial = den_parcial*(x[i] - x[j])
        deno.append(den_parcial)
    return deno

def numerador(x,f):
    num = [1]
    temp = 0
    multi= 1
    for i in range(0, len(x)):
        for j in range(1,len(x)):
            temp = temp - x[j]
            muti = multi*x[j]
        num.append(temp)
        num.append(multi)
    return num"""


#print numerador(x,f)
