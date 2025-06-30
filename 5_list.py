#nested lists
numbers = [1, 2, 3, 4, 5, 6]
newNumbers = [[1, 2, 3], [4, 5, 6]]
# index_1 = newNumbers[1]
# print(index_1)
 #number_6 = index_1[2]
# print(number_6)
 #number = newNumbers[1][2]
# print(number)


 #for li in newNumbers:
   # for num in li:
       # print(num)






copyList = [[print(l) for l in li] for li in newNumbers]

print(copyList)


generatedNestedList = [[newNum for newNum in range(1,4)] for num in range(1,4)]

print(generatedNestedList)