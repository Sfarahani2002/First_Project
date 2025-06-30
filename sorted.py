numbers = [1, 2, 3, 4, 8, 20, 5]
numbers.sort
print(numbers)
result = sorted(numbers, reverse=True) # reverse az akhar b aval
print(result)
users = [
    {'name':'saleh', 'family':'farahani', 'age':123},
    {'name':'ali', 'family':'farahani', 'age':2322},
    {'name':'hassan', 'family':'farahani', 'age':3},
    {'name':'mamad', 'family':'farahani', 'age':234},
]
print(sorted(users,key= lambda user: user['name'])) # + 'age'


#max .py
numberss = [1,4,6,8,90]
print(max(numberss))
chars = ['a', 's' , 'k', 'z']
print(max(chars))
#max.min.py
print(min(numberss))
names = [ 'mammad', 'sasa', 'akbar','aliasghar']
print(max(names))
res = [len(name) for name in names]
print(res)
print(max(names,key= lambda name: len(name)))
print(min(names,key= lambda name: len(name)))


#reversed.py 
num_2 = [ 1,2,3,4,5,6,7]
# num_2.reverse()
print(num_2)
# print(reversed(num_2)) with object
print(list(reversed(num_2)))
print(list(reversed("hi sasa")))
print("hi sasa"[::-1])

nameRec = ''
print(nameRec.join(list(reversed('asas ih'))))
print(nameRec.join(reversed('asas ih')))

for num in reversed(range(0,10)):
    print(num)
    
# sorted
# reverese 
# max
# min