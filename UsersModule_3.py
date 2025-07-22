class User:
    def __init__(self, name, family,age):
        self.name = name
        self.family = family
        self.age = age

    def __repr__(self):
        return f"{self.name} {self.family} is {self.age} years old"
me = User('saleh', 'fr', 23)
you = User('ben','10',22)

print(me)
print(you)

print(type(me))