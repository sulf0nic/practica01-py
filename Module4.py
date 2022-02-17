""" def fun (x, y, z):
    return x+2*y+3*z

print(fun(0,z=1,y=3)) """

""" #ejercicio 2
my_list = ['Mary', 'Had', 'a', 'little', 'lamb']

def my_list(my_list):
    del my_list[3]
    my_list[3]= 'ram'

print (my_list(my_list)) """

""" tuple = (1,2)
tuple2 = (2,3)
my_tuple = (4,5)

my_tuple [1] = tuple[1]+ tuple2[0]
print (my_tuple[1]) """


""" dicctinary = {}
my_list = ['a','b','c','d']
for i in range (len(my_list)-1):
    dicctinary[my_list[i]]= (my_list[i],)

for i in sorted (dicctinary.keys()):
    k=dicctinary[i]
    print(k[0]) """

""" def fun(x):
    global y
    y= x*x
    return y

fun(2)
print(y) """

""" x= None
None != x """

""" #ejercicio 9
def func1_(a):
    return a ** a

def func_2 (a):
    return func1_(a)* func1_(a)

print(func_2(2)) """

""" tup = (1,2,4,8)
tup= tup [1:-1]
tup = tup [0]
print (tup) """

""" #tupla = [1,2]
#tupla.append

def fubnc (a,b):
    return a**b
print(fubnc(2)) """

""" #Ejercicio 13
def function(x=0):
    return x

print(function(1))
 """

"""  #ejecicio 14
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary ['one']

for k in range (len(dictionary)):
    v = dictionary[v]

print(v) """

""" #ejecicio 15
def f(x):
    if x == 0:
        return 0
    return x + f(x-1)

print(f(3)) """

""" #ejercicio 17
def any():
    print(var +1, end='')
var = 1
any()
print (var) """

""" #ejercicio 18
try:
    value = input ("Ingresa un valor:")
    print (value/value)
except ValueError:
    print("Empresa incorrecta..")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea")
except:
    print("Buuu") """

""" #ejercicio 19
def fun(x):
    if x % 2 ==0:
        return 1
    else:
        return

print(fun(1)+1) """

""" #ejercicio 20
def fun (inp=2, out =3):
    return inp *out

print (fun (out=2)) """

""" #ejerecio 22
def fun(x):
    x+=1
    return x

x=2
x=fun(x+1)
print(x) """

""" tupla = (1,2,3)
del tupla[1]
#tupla.append(4)
print(tupla) """

def func(a,b):
    return a**a
print (func(2))