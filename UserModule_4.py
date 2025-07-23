class person:
    classAttribute = "test value"

    def __init__(self, name,family, age):
        self.name = name
        self.age = age
        self.family = family

    def showFullName(self):
        return f'{self.name} {self.family}'

    @classmethod
    def showClassAttribute(self):
        return person.classAttribute

class User(person):
    pass

saleh = person('saleh','fr', 23)
beni = User('beni', 'fa', 22)

print(saleh.name)
print(beni.showFullName())
print(beni.classAttribute)
#print(User.classAttribute)
print(User.showClassAttribute())
