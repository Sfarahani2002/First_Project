myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
doubled_numbers = [num * 2 for num in myNumbers]
#clfor num in myNumbers:
   # doubled_numbers.append(num * 2)

print(myNumbers)
print(doubled_numbers)
myName =" saleh fr"
charName = [char.upper() for char in myName]
print(charName)
even = [num for num in myNumbers if num %2 == 0]
odd = [ num for num in myNumbers if num %2 != 0]
newList =[num * 2 if num %2 == 0 else num *3 for num in myNumbers]
print(even)
print(odd)
print(newList)