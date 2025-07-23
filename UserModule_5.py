class person:

    def __init__(self, name,family,age):
        self.name = name
        self.family = family
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    # getter function
    def get_age(self):
        return self._age

    def set_age(self, ageValue):
        if ageValue >= 0:
            self._age = ageValue
        else:
            raise ValueError('age can not be negative')

    # setter function
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('age can not be negative')

    @property
    def fullName(self):
        return F"{self.name} {self.family}"
    def showFullName(self):
        return F"{self.name} {self.family}"
me = person('saleh','fr' ,23)
print(me.get_age())
# me.age = -1
# me.set_age(-2)
# me.set_age(23)
print(me.get_age())
print(me.age)
me.age = 40
print(me.age)

print(me.showFullName())
print(me.fullName)