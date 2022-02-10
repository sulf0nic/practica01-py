def printHello (fistName, lastName):
    print("Hola", fistName,lastName )

printHello ("Pedro", "Carranza")
printHello (fistName="Pedro", lastName="Cano")

def validarINE(name, edad =18):
    print ("INE de ", name, edad)

validarINE("Pedro")

def validarINE1(name, edad= int(input("edad "))):
    print ("INE de ", name, edad)
validarINE1("Pedro")