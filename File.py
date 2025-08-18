testTextFile = open("./text.txt")

print(testTextFile.read())
testTextFile.seek(0)
print(testTextFile.read())
print(testTextFile.read())

print(testTextFile.read())
print(testTextFile.read())

textLines = testTextFile.readlines()
print(textLines)

testTextFile.close()
print(testTextFile.closed)
print(testTextFile.closed)

# print("hello my name is saleh") => /n = new line

with open("./text.txt") as file:
    print(file.read())
    file.seek(0)
    print(file.read())

with open("./text.txt", mode='w') as file:
    file.write(" this is edited text\n")

with open("./text.txt", mode='a') as file:  #=> append
    file.write(" this is new test text")

