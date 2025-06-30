numbers = [ 1, 2, 3, 4, 5]
dublles = map(lambda x : x * 2 , numbers)
print(list(dublles))

names = ["mohammad", "saleh" , "asqar"]
upperNames = map(lambda name: name.upper() ,names)
print(list(upperNames))


people =[
    {'name':'saleh' , 'family': 'farahani', 'age' : 23},
    
{'name':'ragnar' , 'family': 'boomi', 'age' : 23},
{'name':'ali' , 'family':'alizade' , 'age' : 23},
]
    
families = map(lambda person : person['family'], people)
print(list(families))
# print(list(map(lambda person : person['family'], people)))
family_2 = []
for person in people:
    family_2.append(person['family'])
print(family_2)