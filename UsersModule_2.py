class User:
    activeUsersCount = 0

    def __init__(self,name,family):
        self.name = name
        self.family = family
        User.activeUsersCount += 1
        print(f"{self.name} is now active")
    def loggedInUsers(self):
        self.activeUsersCount -= 1
        print(f"{self.name} has logged in")

    @classmethod
    def getActiveUsersCount(cls):
        print(f"there are currently {cls.activeUsersCount} active users")
    @classmethod
    def from_string(cls, string_data):
       # data = string_data.split(',')
        name, family = string_data.split(',')
        return cls(name,family)
       # return cls(data[0],data[1])

User.getActiveUsersCount()
me = User('saleh','fr')
you = User('ben', '10')
# me.getActiveUsersCount()
User.getActiveUsersCount()

newIstance = User.from_string('saleh , fr')
print(newIstance.name, newIstance.family)