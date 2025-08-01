class IUserService:
    def getAllUsers(self): raise NotImplementedError

    def getUserById(self): raise NotImplementedError

    def createnewUser(self): raise NotImplementedError

class UserServiceBySql(IUserService):
    def getAllUsers(self):
        print('get all users from sql  server')

    def getUserById(self):
        print('get user by id from sql server')

    def createnewUser(self):
        print('create new user from sql server')

class UserServiceByOracle(IUserService):
    def getAllUsers(self):
        print('get all users from oracle')

    def getUserById(self):
        print('get user by id from oracle ')


    def createnewUser(self):
        print('create new user from oraclr ')


userService = UserServiceBySql()
userService_by_oracle = UserServiceByOracle()
userService_by_oracle.getAllUsers()
userService.getAllUsers()
userService.createnewUser()


