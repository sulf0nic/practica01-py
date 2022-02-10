variable = 1
variablefloat =3.4
print (variable)
print (type(variable))
print (type(variablefloat))
variableString = "esto es una cadena"
print (variableString)
variableboolean = True 
lista = [1,2,3,4,5]
print (lista)
print (type(lista))
tupla = (1,2,3,4,4,5)
print (type(tupla))
dicionario = {"nombre" : "Jesus", "edad" :30, "empleo" :"professor"}
print (type(dicionario))
print (dicionario)

for numero in range (len (lista)):
    print(numero)
#print(sum(1, 2))
sumaCorta = lambda x,y : x+y 
print (sumaCorta(3,5))
x=0
listafiltrada = list(filter(lambda x:x, x>3 , lista))