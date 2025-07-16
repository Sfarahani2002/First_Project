from Toplearn.UserModule import User
saleh = User('saleh', 'fr',23,)
aliReza = User()
print(f"{saleh.userName} {saleh.userFamily} {saleh.userAge}")
print(f"{aliReza.userName} {aliReza.userFamily} {aliReza.userAge}")
print(saleh.buyCourse())
print(saleh.articles())
print(saleh.getUserBirthDate())