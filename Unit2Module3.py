""" #ejercicio 1 impime 2
class A:
    def __init__(self, v= 1):
        self.v =v
    
    def set(self, v):
        self.v =v
        return v
a = A()
print(a.set(a.v+1)) """

""" # Ejercicio 2 imprime 3
try:
    raise Exception (1,2,3)
except Exception as e:
    print(len(e.args)) """

""" #ejecricio 3, imprime 3
class A:
    X =0
    def __init__(self, v = 0):
        self.Y =v
        A.X += v
a = A()
b = A(1)
c = A(2)
print (c.X) """

""" #ejecricio 5 imprime A
class A:
    def __str__(self):
        return 'a'

class B:
    def __str__(self):
        return 'b'

class C(A,B):
    pass

o = C()
print(o) """

""" class A:
    def __init__(self):
        self.a = 1

class B(A):
    def __init__(self):
        A.__init__()
        self.b = 2 """

""" #ejecrcio 7    imprime b
class A:
    def a (self):
        print ('a')

class B:
    def a (self):
        print ('b')        

class C(B,A):
    def c(self):
        self.a()
p = C()
p.c() """
""" 
#ejecicp 8 respues bcac
def f(x):
    try:
        x=x/x
    except: 
        print ("a",end='')
    else: 
        print ("b",end='')
    finally: 
        print ("c",end='')
f(1)
f(0) """

""" #ejercicio 9 respuesta atribute error
class A:
    def __init__(self,v):
        self.__a = v +1
a =A(0)
print(a.__a) """

""" #ejercicio 10 imprime 1
class A:
    v=2

class B(A):
    v=1
class C(B):
    pass
o =C()
print(o.v) """

""" #ejercicio 11 imprime b

class A:
    def __str__(self):
        return 'a'

class B(A):
    def __str__(self):
        return 'b'

class C(B):
    pass
o =C()
print (o) """

""" #objet = class()
class Class:
    def __init__(self):
        pass

object = Class() """

""" #JERCICIO 15 GENERA UN ERROR
class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a,'A')) """

""" #IMPRME TRUE
class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(C,A)) """
""" 
class A:
    A =1

print(hasattr (A,'A')) """