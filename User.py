#_name
# --name => name mangling
# __name__


class User:
    def __init__(self, userName):
        self.userName = userName
        self._password = "456"
        #
        self.__messege ="i love barca"

    def login(self, gotPassword):
        if self._password == gotPassword:
            print("Login Successful")
        else:
            print("Login Failed")

class person:
    def __init__(self):
        self.__messege = "test messege"

me = User("saleh")
you = person()

you._person__messege
print(me._User__messege)
#print(dir(me))

