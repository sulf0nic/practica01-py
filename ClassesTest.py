#RICARDO DANIEL ARENAS CARRANZA
#Matricula M01009381
#BASES DE PROGRAMACIÓN (221203033/CMX)

from Dog import Dog

dog = Dog("Pastor", 23, "Blanco", "Pistachon",3,"8484")
dog1 = Dog("Husky", 33, "Gris", "Kiara", 4,484848)
dog2 = Dog("Snahuzer", 43, "Sal y pimienta", "Maya",5, 38484884)
dog3 = Dog("Bull Dog", 23, "Cafe", "Doggy",6,9494)

print(dog.printInfo())
print(dog1.printInfo())
print(dog3.printInfo())
print(dog2.printInfo())

dog.size = 29
dog.name = "Chilakil"

print(dog.printInfo())
print(dog1.printInfo())
print(dog3.printInfo())
print(dog2.printInfo())

        