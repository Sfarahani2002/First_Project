me = {
    "name": "saleh",
    "family": 'farahani',
    "age": 23
}
isExist = "name" in me
print(isExist)
print(me["family"])

if "eye" in me:
    print(me["eye"])
else:
    print("there is no eye in me")
    
    isNameExsit = "saleh" in me.values()
    print(isNameExsit)
    
    
    me.clear
    copy_me = me.copy
    me.fromkeys
    
    
    print(me["name"]) 
    print(me.get("name"))
    
    
    
    isPhoneExist = me.get("phone")
    print(isPhoneExist is None)
    print(isPhoneExist)