# poly => multi
# morph => form
class Animal:
    def makeSound(self):
        raise NotImplementedError
class Dog(Animal):
   # pass
    def makeSound(self):
       return "dog makes sound"

class Cat(Animal):
   # pass
    def makeSound(self):
         return "cat makes sound"

class Wolf(Animal):
   def makeSound(self):
       return "wolf does not make any sound"

wolf = Wolf()
dog = Dog()
cat = Cat()
print(dog.makeSound())
print(cat.makeSound())
print(wolf.makeSound())
































# numbers = [1,2,3,4,5,6,]
# myNum = {1,2,3,4,5,6,}
# person = {
#     'name' : 'saleh' ,
#     'family' : 'fr'
# }
#
# numbers.copy()
# myNum.copy()
# person.copy()
# print(len(numbers))
# print(len(myNum))
