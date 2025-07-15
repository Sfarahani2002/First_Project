class User:
    userName = "Saleh"
    userFamily ="farahani"
    userAge = 23

    def showFullName(self):
        return f"{self.userName} {self.userFamily}"
    def __init__(self, userName, userFamily):
        self.userName = userName
        self.userFamily = userFamily


numbers = list()
Saleh = User("Saleh","farahani")
asqar = User("asqar","movafaqiat")
print(Saleh.showFullName())
print(asqar.showFullName())


print(Saleh.userName + " " + Saleh.userFamily)