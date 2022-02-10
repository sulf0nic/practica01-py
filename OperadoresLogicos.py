#RICARDO DANIEL ARENAS CARRANZA
#Matricula M01009381
#BASES DE PROGRAMACIÓN (221203033/CMX)

from turtle import color


number = 50

#print(number == 50 & number> 20)
#print(number == 50 and number> 20)

def comprar ():
    color = "red"
    if color == "red" or color == "blue":
        return "comprar"
    else: 
        return "no comprar"

print (comprar())

print (not number == 50)
print (not number != 50)