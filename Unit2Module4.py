""" #ejecicio 1 regresa ***
def o(p):
    def q():
        return '*' * p
    return q

r = o(1)
s = o (2)
print(r()+s()) """

""" #Ejercicio 3 devuelve ['large', 'medium', 'small']
import os 
os.mkdir('thumbnails')
os.chdir('thumbnails')
sizes = ['small', 'medium', 'large']
for size in sizes:
    os.mkdir(size)

print (os.listdir()) """

""" #ejercico 6 devuelve 19/November/27 11:27:22
from datetime import date, datetime
datetime = datetime(2019,11,27,11,27,22)
print(datetime.strftime('%y/%B/%d %H:%M:%S')) """

""" #EJERCICIO 7 DEVUELVE 345 days, 0:00:00
from datetime import date
date_1= date (1992,1,16)
date_2 =date(1991,2,5)
print(date_1 - date_2) """

""" #ejercico 8 devuelve Mo Tu We Th Fr Sa Su
import calendar 
print (calendar.weekheader(2)) """

""" #ejecicio 9 DEVUELVE 0123456
import calendar
c = calendar.Calendar()
for weekday in c.iterweekdays():
    print(weekday, end='') """

""" #ejectcio 10 devuelve ace
def I():
    s = 'abcdef'
    for c in s [::2]:
        yield c

for x in I():
    print (x,end='')
 """
""" 
#ejecicio 11  devuelve /Users/ricardo-arenas/Documents/ebc-python/practica01-py/Pictures
import os 
os.mkdir('Pictures')
os.chdir('Pictures')
os.mkdir('Thumbails')
os.chdir('Thumbails')
os.mkdir('tmp')
os.chdir('../')

print(os.getcwd()) """
""" 
#ejercicio 12 imprime ++++++%
def fun(n):
    s = '+'
    for i in range (n):
        s+= s
        yield s
for x in fun(2):
    print (x, end='') """
""" 
#ejercicio 13 imprime bytearray(b'\x00\x00\x00')
b= bytearray(3)
print(b) """

""" #ejecicio 14 devuelve foo = tuple (map(lambda x:x **x, my_list))
my_list = [1,2,3]
foo = tuple (map(lambda x:x **x, my_list))
print (foo) """

""" #ejerccio 16 devuelve foo = list (filter(lambda x: x-0 and x-1, my_tuple))
my_tuple = (0,1,2,3,4,5,6)
#foo = list (filter(lambda x: x==0 and x==1, my_tuple))
foo = list (filter(lambda x: x-0 and x-1, my_tuple))
print(foo) """
