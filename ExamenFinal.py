# #imprime 0
# d = {1: 0, 2:1, 3:2, 0:1}
# x = 0 
# for y in range (len(d)):
#     x =d[x]

# print(x)    

#imprime a'b'c
#print("a", "b", "c", sep="'")

# #imprime a
# class A:
#     def a (self):
#         print ('a')

# class B:
#     def a (self):
#         print ('b')

# class C(A,B):
#     def c (self):
#         self.a()

# o=C()
# o.c()

# #error
# class A:
#     def __init__(self):
#         pass
#     def f(self):
#         return 1

#     def g():
#         return self.f()
# a=A()
# print (a.g())

# #marca error
# import os 
# os.makedirs('Pictures/Thumbails')
# os.rmdir('Pictures')


# #imprime ac
# try:
#     raise Exception
# except BaseException:
#     print("a", end='')
# else:
#     print("b", end='')
# finally:
#     print ("c")

# #devuelve tru false
# a = True
# b = False
# a = a or b 
# b = a and b 
# a = a or b
# print(a,b)

# #devuelve 6 0 1 2 3 4 5
# import calendar 
# c =calendar.Calendar(calendar.SUNDAY)
# for weekday in c.iterweekdays():   
#     print (weekday, end=" ") 

# str1= 'string'
# str2 = str1[:]
# print (str1, str2)

# #devuelve 1
# class A:
#     def __init__(self,v):
#         self._a = v+1
    
# a =A(0)
# print(a._a)

# #[2, 4, 6, 8]
# my_list = [1,2,3,4]
# my_list =(list(map(lambda x:2 *x, my_list)))
# print(my_list)


# #devuelve 12 3
# x, y , z=3,2,1
# z,y,x = x,y,z
# print(x,y,z)

# #imprime 14 days, 11:00:00
# from datetime import timedelta
# delta = timedelta(weeks=1, days=7, hours=11)
# print (delta)

# #imprime 3
# t =(1,2,3,4)
# t= t[-2:-1]
# t =t [-1]
# print (t)

# #el codigo es erroneo
# def fun (par2, par1):
#     return par2 + par1

# print (fun(par2=1))

# #DEVUELVE FALSE TRUE
# class X:
#     pass

# class Y(X):
#     pass

# class Z(Y):
#     pass

# x=X()
# z= Z()
# print(isinstance(x,Z), isinstance(z,X))


# #123
# d  = {'one': 1, 'three': 3, 'two': 2}
# for k in sorted(d.values()):
#     print(k,end='')

#True True
#print("bobn".isalpha())

# #imprime 3.5
# v = 1+1 //2+1/2+2
# print(v)

#dev1
#print(len((1,)))

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
# print(issubclass(C,A) and issubclass(C,B))

# #devuelve **
# def a(x):
#     def b():
#         return x + x
#     return b

# x= a('x')
# y = a('')
# print(x()+y ())


# #dev <__main__.A object at 0x104b78340>
# class A:
#     def __init__(self,name) :
#         self.name = name

# a=A("class")
# print(a)

# #dev true false
# st1 ='Bond'
# str2 = 'James Bond'

# print(st1.isalpha(),str2.isalpha())

#dev 0
#print (len([i for i in range (0,-2)]))

# #dev 24
# d = {}
# d['2']=[1,2]
# d['1']= [3,4]

# for x in d.keys():
#     print(d [x][1],end="")

# #dev True
# z=2
# y=1
# x=y <z or z>y and y>z or z <y

# print(x)

# #True
# class A:
#     A=1
#     def __init__(self):
#         self.a=0

# print(hasattr( A,"A"))

# #dev 2019/11/27 11:27:22
# from datetime import  datetime
# datetime = datetime(2019,11,27,11,27,22)
# print(datetime.strftime('%Y/%m/%d %H:%M:%S')) 


# #devuvleve 2 lineas vacias
# my_list = [[c for c in range (r)]for r in range(3)]
# for element in my_list:
#     if len(element)<2:
#         print()


# #dev un error
# my_string = 'abcdef'

# def fun (s):
#     del s[2]
#     return s

# print (fun (my_string))

# #devuelve 2
# t = (1, )
# t=t [0]+t [0]
# print (t)


# #devuelve 1
# x = """
# """
# print(len(x))

# #devuvle 5
# class A:
#     A=1
#     def __init__(self, v=2 ) :
#         self.v = v +A.A
#         A.A += 1
        
#     def set(self, v):
#         self.v+=v
#         A.A += 1
#         return
    
# a =A()
# a.set(2)
# print(a.v)

# #imprime *
# i =4 
# while i>0:
#     i -= 2
#     print("*")
#     if i == 2:
#         break
# else:
#     print("*")


# #devuelve *****
# x= 16
# while x >0:
#     print('*', end='')
#     x //= 2


#devuelve 

def fun(x):
    return 1 if x % 2 != 0 else 2
print(fun(fun(1))) 
