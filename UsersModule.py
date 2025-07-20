class User:
    activeUsersCount = 0

    def __init__(self,userName,userFamily):
        self.name = userName
        self.family = userFamily
        User.activeUsersCount += 1
        print(f"{self.name} logged in ")

    def logOut(self):
        print(f"{self.name} has logged out")
        User.activeUsersCount -= 1

print(f"active users : {User.activeUsersCount}")
saleh = User('saleh','fr')
ali = User('ali','hs')

print(f"active users : {User.activeUsersCount}")
ali.logOut()

print(f"active users : {User.activeUsersCount}")