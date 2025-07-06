# try:
#     print(myName)
# except:
#     print('an error occures')
# #-----------------------------------------
# # def get(dic,key):
# #     return dic[key]
# #-----------------------------------------
# #print(get(person, 'name'))   
# person= {
#     "name": "saleh",
#     'family':"Fr"
# }
#-------------------------------------------
# def get(d,key):
#         try:
#             return d[key]
#         except key: 
#             return "no key found"
#         except IndexError:
#             return 'no indexError'

# print(get(person,"name"))
# print(get(person,"age"))
#--------------------------------------------
# try:
#     num = int(input('please inter a number: '))
# except:
#     print('thats not a number!')
# else:
#     print('this is else section')
# finally:
#     print('thisis finally section')
#---------------------------------------------
while True:
  try:
      num = int(input('please inter a number: '))
  except :
      print('thats not a number! please enter another one :')
  else:
     print('you have entered a number')
     break
  finally:
     print('this is finally section')
     
 #----------------------------------------------
 def divide(first, second):
     try:
         return first / second
     except ZeroDivisionError:
         return('Dont divided by zero !!')
     except TypeError as error:
         print(error)
         return('first and second must be num !!!')
     
print(divide(10,2))
#----------------------------------------------