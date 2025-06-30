#def exponent ( num, power=3): #=3 difult
    #return num ** power

3#print(exponent(2, 10))
#print(exponent(2))
#.pop # delet 1 index
#def showFullName (first, last):
   # return f"{first} {last}"
#print(showFullName("saleh", "ffarahani"))
#print(showFullName(last="farahani",first="saleh"))




#def sum_all_numbers(*args):
    #print(args)
  #  total = 0 
   # for num in args:
   #     total += num
  #  return total
#number =[1,3,4,6,7,8]

#print(sum_all_numbers(*number))
#print(sum_all_numbers(1,3,5,8))



def showUserInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
showUserInfo(name="saleh", famili="farahani", age=23)

#parameters
#*args
#defulat parameters
#**kw args
def display_info (a,b,*args,defpara = "defulat", **kwargs):
    return [a,b, args, defpara, kwargs]
print(display_info(1,2, 3, first_name= 'saleh', last_name='farahani' ))




def display_names(name, famili):
    print(f"name is {name} famili is {famili}")
person = {"name": "saleh","famili":"farahani"}
display_names(**person)