class Car:
    def move(self):
        raise NotImplementedError()

class Benz(Car):
    def __init__(self,model):
        self.model = model

    def move(self):
        print(f"{self.model} is moving")


class Bmw(Car):
    def __init__(self, model):
        self.model = model

    def move(self):
        print(f"{self.model} is moving")

class Porshe(Car):
    def move(self):
        print(f"porshe is moving")


sls = Benz('sls')
x4 = Bmw('x4')
macan = Porshe()

sls.move()
x4.move()
macan.move()