class User:
    activeUsersCount = 0
    allowedUsers = ['saleh','ali','mahdi','ben']
    loggedInUsers = []

    def __init__(self,userName,userFamily):
        if userName not in User.allowedUsers:
            raise ValueError('Invalid username')
        self.name = userName
        self.family = userFamily
        User.activeUsersCount += 1
        User.loggedInUsers.append(userName)
        print(f"{self.name} logged in ")

    def logOut(self):
        print(f"{self.name} has logged out")
        User.activeUsersCount -= 1
        User.loggedInUsers.remove(self.name)

saleh = User('saleh','fr')
print(f"active users : {User.activeUsersCount}")
print(User.loggedInUsers)

ali = User('ali','hs')

print(f"active users : {User.activeUsersCount}")
print(User.loggedInUsers)
ali.logOut()
saleh.logOut()

print(f"active users : {User.activeUsersCount}")
print(User.loggedInUsers)