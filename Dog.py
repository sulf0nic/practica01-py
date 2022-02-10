from Animal import Animal 

class Dog(Animal):   
    def __init__(self, name, size, color, race, age,id):
        super().__init__(name, age)
        self.id = id
        self.size = size
        self.color = color
        self.race = race

    def printInfo(self):
        print(self.race, self.size, self.color, self.id,self.getAge(),self.getName())