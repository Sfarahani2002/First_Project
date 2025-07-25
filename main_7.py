class person:
    def __init__(self,name,family):
        self.name = name
        self.family = family

    @property
    def fullName(self):
        return f"{self.name} {self.family}"

class User(person):
    def __init__(self,name,family,email):
        super().__init__(name,family)
       # person.__init__(self,name,family)
        self.email = email

saleh =User('saleh','fr','theend@.com')
print(saleh.fullName)