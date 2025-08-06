class person:
    def __init__(self, name, family, age, money):
        self.name = name
        self.family = family
        self.age = age
        self.money = money
    def __repr__(self):
        return f'{self.name} {self.family}  {self.age}'

    def __len__(self):
        return self.age

    def __add__(self, other):
        return self.money + other.money

    def __mul__(self, other):
        return self.money * other.money

    def __truediv__(self, other):
        return self.money / other.money


person_1 =  person('saleh', 'fr', 23,500)
person_2 =  person('beni', 'fa', 22, 2000)
print(person_1)
print(len(person_1))
print(person_1 + person_2)
print(person_1 * person_2)
print(person_1 / person_2)