from sympy import*

f = ""

print
print ("Super calculo de integrales multiples con el metodo de simpson c:")
print
f = raw_input("Ingrese su funcion f(x,y):\n")
print
funcion = sympify(f)
ax = input("Ingrese su parametro inicial:\n")
bx = input("Ingrese su parametro final:\n")
ay = input("Ingrese su parametro inicial:\n")
by = input("Ingrese su parametro final:\n")

mx = input("Ingrese el numero de particiones:\n")
my = input("Ingrese el numero de particiones:\n")

def simpson_multiple(f,funcion,ax,bx,ay,by,mx,my):
  dy = (by - ay)/ float(my)
  v = ay
  r = []
  gxay = f.replace("y", "a")
  for i in range (0,my+1):
    #gx = gxay.evalf(subs =  {"a" : v})
    print gxay
    u = simpson(gxay,ax,bx,mx,v)
    r = r+[u]
    v = v +dy
  s = 0
  for i in range(0,my):
    s = s*2(2- (i+1)%2)*r[i]
  s = (dy/3) * (r[0] + s + r[my])
  return s


def simpson(funcion,a,b,m,v):
  print v
  h = (b-a)/float(m)
  s = 0
  x = a
  for i in range(1,m):
    n = x + (i*h)
    n_evaluado = funcion.evalf(subs = {"x" : n , "a" : v})
    s = s + 2*(i%2+1)*n_evaluado
  a_evaluado = funcion.evalf(subs = {"x" : a , "a" : v})
  b_evaluado = funcion.evalf(subs = {"x" : b , "a" : v})
  resul = h/3 * (a_evaluado + s + b_evaluado)
  return resul

def main():
  print simpson_multiple(f,funcion,ax,bx,ay,by,mx,my)

if __name__ == "__main__":
  main()
