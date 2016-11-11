E = 2.718281828
x = 0.5
datos = [x]
error = []
print("")
print ("Datos")
for i in range(0,15):
    x = E**(-x/2)
    datos.append(x)
    print x
    error.append(abs(datos[i]-datos[i+1]))
print("")
print("Errores")
for i in range(0,15):
    print(error[i])
print("")
