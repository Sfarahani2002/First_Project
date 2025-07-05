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
try:
    num = int(input('please inter a number: '))
except:
    print('thats not a number!')
else:
    print('this is else section')
finally:
    print('thisis finally section')