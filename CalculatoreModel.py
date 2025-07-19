class Calculator:
    def sum(self,a,b):
        print(f"{a} + {b} : {a+b} ")
    def subtract(self,a,b):
        print(f"{a} - {b} :{a-b} ")
    def multiply(self,a,b):
        print(f"{a} * {b} :{a*b} ")
    def divide(self,a,b):
        print(f"{a} / {b} :{a/b} ")

myCalc = Calculator()
myCalc.sum(24,8)
myCalc.subtract(24,8)
myCalc.multiply(24,8)
myCalc.divide(24,8)

