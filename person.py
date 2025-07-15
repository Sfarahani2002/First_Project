class Car:
    def __init__(self,name,numberOfDoors,color):
        self.name = name
        self.numberOfDoors = numberOfDoors
        self.color = color
    def showCarFullInfo(self):
        return f"car name is {self.name} & car color is {self.color}"

benz = Car("Benz",2,"blue")
bmw = Car("BMW",2,"black")
print(bmw.showCarFullInfo())
print(benz.showCarFullInfo())
print(bmw.color)