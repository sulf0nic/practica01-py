""" class Class:
    def __init__(self, val=0):
        pass
object=Class()
print(object) """

""" #devuelve la ruta
import os
os.mkdir('pictures')
os.chdir('pictures')
print(os.getcwd()) """

#print(__name__)

""" #imprime a
try:
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print ("c") """

""" #devuelve ***
def o(p):
    def q():
        return '*' * p
    return q

r =o(1)
s = o(2)
print(r() +s()) """


""" #devuvelve foo = map (lambda num:num ** 2, numbers)

numbers = [0,2,7,9,10]
#foo = filter (lambda num:num ** 2, numbers)
foo = map (lambda num:num ** 2, numbers)
print(list(foo)) """

""" #28 days, 22:00:00
from datetime import timedelta
delta = timedelta(weeks=1, days=7, hours=11)
print (delta *2) """

""" #devuelve error
class A:
    def __init__(self):
        pass

a = A(1)
print (hasattr(a,'A')) """

""" #harwware y sysname
import os 
os.mkdir('pictures')
os.chdir('pictures')
print(os.uname()) """

#print (float("1.3"))

"""
#imprime 2
 x = "\\\\"
print(len(x)) """

""" #DEVUELVE FALSE
class A:
    pass

class B(A):
    pass
class C(B):
    pass
print(issubclass(A,B)) """

""" #DEVUVLEVE AttributeError
class A:
    def __init__(self, v):
        self.__a = v+1

a =A(0)
print(a.__a) """


""" #DEVUVELVE 3
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args)) """

""" ##devuvle 3

class A:
    def __init__(self, v =2):
        self.v = v
    
    def set(self, v=1):
        self.v += v
        return self.v
a = A()
b = a
b.set()
print(a.v) """

""" 
#eeroro por que va al ultimo exception
try: 
    raise Exception
except: 
    print("c")
except BaseException:
    print("a")
except Exception:
    print("b") """

#key = bytes([0x13, 0x00, 0x00, 0x00, 0x08, 0x00])

""" #DEVUELVE Sun Mon Tue Wed Thu Fri Sat
import calendar 
calendar.setfirstweekday(calendar.SUNDAY)
print (calendar.weekheader(3)) """

""" #devuelve r
print (chr (ord ('p')+2)) """

#devuvle

""" class I:
    def __init__(self) :
        self.s = 'abc'
        self.i =0

    def __inter__ (self):
        return self

    def __next__ (self):
        if self.i == len (self.s):
            raise StopIteration
        v = self.s [self.i]
        self.i += 1
        return v

for x in I():
    print(x, end='') """

""" #devuvelve False
class A:
    A= 1
    def __init__(self):
        self.a =0

print(hasattr(A,'a')) """

""" import math
print(dir(math)) """

""" #error
x = "\\\"
print(len(x))  """
