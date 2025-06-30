item1 = "saleh"
item2 = "mohsen"
item3 = "hossein"
item4 = "fatem"
mylist =(item1, item2, item3, item4)
#print(mylist)
#print(len(mylist))
#print(mylist[2])
myRange = range(30)
#print(list(myRange))
#print(mylist[-3])
isExistmohsen = "mohsen" in mylist
myColors = ["red","blue","gray","green","yellow","orange",3.6]
for color in myColors:
    if type(color) == str:
        print(f"the color is : {color} ")
    else:
        print(f"{color} is not a color")

print("-------------------------")
index = 0
while index < len(myColors):
    color = myColors[index]
    if type(color) == str:
        print(f"the color is : {color}")
    else:
        print(f"{color} is not a color")

    index += 1 