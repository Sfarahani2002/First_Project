class person:
    def __init__(self,name):
        print("Person Init")
        self.__name = name

    def sayHello(self):
            return f"Hello {self._person__name} in person class "

    def sayBye(self):
        return f"goodBye {self._person__name} "

class User:
    def __init__(self, name):
        print("User Init")
        self.__name = name

    def sayHello(self):
        return (f"Hello {self._User__name} in User class ")

class Admin(person,User):
    def __init__(self,name):
        print("Admin Init")
        print(f"got name is {name}")
        #super().__init__(name)
        User.__init__(self,"user name")
        person.__init__(self,"person name")

person_1 = Admin('saleh')

# __mro__   -> method resolution order
# mro()
# hrlp(cls)

print(Admin.__mro__)
print(Admin.mro())
help(Admin)





#print(person_1.sayBye())
#print(person_1._person__name)
#print(person_1._User__name)
#print(person_1.name)
#print(person_1.sayHello())
#print(isinstance(person_1,person))
#print(isinstance(person_1,User))
#print(isinstance(person_1,Admin))