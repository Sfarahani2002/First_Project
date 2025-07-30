#method resolution order
# __mro__
# mro()
# hrlp(cls)

class A:
    def say_hi(self):
        print("hi python in A")

class B(A):
    pass
    #def say_hi(self):
        #print("hi python in B")

class C(A):
    pass
   # def say_hi(self):
        #print("hi python in C")

class D(B,C):
    pass
   # def say_hi(self):
      #  print("hi python in D")

item = D()
item.say_hi()

print(help(D))