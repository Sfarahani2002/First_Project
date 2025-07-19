class User:
    def __init__(self,gotName,gotFamili,gotAge):
        self.Name = gotName
        self.Family = gotFamili
        self.Age = gotAge

    def showFullName(self):
        return f"{self.Name} {self.Family}"
        #return self.Name + " " + self.Family

    def userAgeStatus(self):
        return "adult" if self.Age >= 18 else "teenager"

me = User('saleh','fr',23)
print(me.showFullName())
print(me.userAgeStatus())