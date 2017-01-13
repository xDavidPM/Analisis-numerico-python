def lagrange(x,y,t):
    n = len(x)
    m = len(y)
    z = []
    s = 0
    for i in range(0,m):
        L =0
        for j in range(0,n):
            for k in range(0,n):
                if (j != k):
                    L = L*((t-x[k]) / (x[i] - x[j]))
        s = s + L*f[i]
    return s

x = [0,0.2,0.5,0.8,1]
y = [1,1.2214,1.648721271,2.225540928,2.719291928]
t = 0.7
print (lagrange(x,y,t))
