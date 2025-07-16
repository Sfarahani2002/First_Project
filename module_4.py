class User:

    def __init__(self, gotUserName, gotUserFamily, gotUserEmail, gotUserPass):
        self.UserName = gotUserName
        self.UserFamily = gotUserFamily
        self.UserEmail = gotUserEmail
        self.UserPass = gotUserPass

    def buyCourse(self):
        return (f"{self.UserName} can buy all courses")
    def readArticles(self):
        return (f"{self.UserName} can read all articles")
    def getUserBirthDate(self):
        return 2019 - self.userAge