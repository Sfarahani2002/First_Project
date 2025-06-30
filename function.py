def sayhello():
    #print("hello")

#sayhello()

#def square_of_7():
    print("i am saleh befor")
    a = 18 
    b = 1
    return a + b

#print(square_of_7())

def sum (number_1, number_2):
    return number_1 + number_2

#print(sum(12, 9))


Name = 'saleh'
famili = 'farahani'
def showFullName (firstName,lastName):
    return firstName + " " + lastName

#print(showFullName(Name, famili))



person = {
    "name" : "saleh",
    "famili" : "farahani"
}
#print(showFullName(person["name"],person["famili"]))




def divide (num_1, num_2):
    return num_1 / num_2
#print(divide(16, 4))



#myNumber = [1,2,3,4,5,6,7,8,9]
#def sum_odd_number(number):
    total = 0
    for num in myNumber:
        if num % 2 != 0:
            total += num
    return total
#print(sum_odd_number(myNumber))

def is_even_number(number):
    if number % 2 == 0:
        return True
    #else:
       #return false
    return False
print(is_even_number(5))
print(is_even_number(6))