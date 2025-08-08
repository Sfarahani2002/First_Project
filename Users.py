class User:
    ActiveUsers = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        userDict = {'name':name, 'age':age}
        self.ActiveUsers.append(userDict)
        self.index = 0

    def log_out(self):
        print(f"{self.name} is now logged out")
        currentUser = list(fillter(lambda user: user['name'] == self.name, User.ActiveUsers))
        print(currentUser)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(User.ActiveUsers):
            person = User.ActiveUsers[self.index]
            self.index += 1
            return person
        raise StopIteration

person_1 = User('saleh', 23)
person_1 = User('bani', 22)
person_1 = User('banisa', 2)

#print(User.ActiveUsers)

for person in person_1:
    print(person)