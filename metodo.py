#el medoto simpson
#import sympy
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt



px = []
py = []
def metodo_simp(fund,a,b,n):
    ini = min(a,b)
    fin = max(a,b)
    a = ini
    b = fin
    h = (b-a)/n
    i = 0
    px = []
    py = []
    global px
    global py
    while( a+i*h <= b ):
        p = a+i*h
        px.insert(i,p)
        py.insert(i,funcion.subs(x,p).evalf())
        i+=1
        pass
    j=1
    fi = 0
    print ( px,py,i )
    while( j<=i-2 ):
        fi = fi + py[j]
        j+=2;
    j=2
    fp = 0
    while( j<=i-3 ):
        fp = fp + py[j]
        j+=2;
    r = (h/3)*(py[0]+4*fi+2*fp+py[i-1])
    return ("---"+str(r))
    pass



x, y  = symbols('x y')
funcion = parse_expr( input("ingrese funcion :") )
a  = int ( input("ingrese a : ") )
b  = int ( input("ingrese b : ") )
n  = int ( input("ingrese n : ") )
print( metodo_simp(funcion,a,b,n) );
#dominio = np.linspace(-10,10,100)
#d = np.linspace(a,b,100)
#rag = convercion()
#Y1 = np.asarray( [funcion.subs(x,valor) for valor in dominio ] )
#print ( Y1,dominio)
#print ( type(Y1),type(dominio))
func = lambdify(x, funcion ,'numpy')
print (func)
dominio = np.linspace(-10,10,1000)
Y1 = func(dominio)
d = np.linspace(a,b,1000)
rag = func(d)
plt.figure()
plt.plot(dominio,Y1,'g-')
plt.plot(px,py,'ro')
plt.fill_between(d,rag)
plt.show()
print ( px, py )
