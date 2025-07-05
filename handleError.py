try:
    print(myName)
except:
    print('an error occures')
#-----------------------------------------
def get(dic,key):
    return dic[key]
    
print(get(person, 'name'))   
person= {
    "name": "saleh",
    'family':"Fr"
}
#print(person["name"])