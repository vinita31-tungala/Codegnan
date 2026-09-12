# Dictionary - key-value pairs
a={"num":"B7","name":"vinita","course":"python","cgpa":"8.9","addr":"Vekanuru"}
print(a)
print(a["num"])
print(a["name"])
print(a.get("salary"))
# Adding a new key
#dict_name["new_key"]="value"
a["conc_num"]="1234567890"
print(a)
#Updating a value
a["conc_num"]="0123456789"
print(a)
#I need to print only keys
print(a.keys())
print(a.items())    # To print both keys and values

for key,value in a.items():   # Using for loop(for not getting the data in brackets)
    print(key,value)
# pop()
a.pop("name")
print(a)
# clear()
'''a.clear()
print(a)'''
#max(), min(), sorted(),len()
print(len(a))
v={"1":"a","2":"b","3":"c"}
print(max(v))
print(min(v))
print(sorted(a))
a["num"]="A8"
print(a)
# create a dict on your own data(id,name,cgpa,college),print all the key-value pairs,modify email,cgpa,college name in short-form,sorted()
stu={"id":"B7","name":"vinita","cgpa":"8.9","college":"NRIIT","email":"vini@gmail.com"}
print(stu)
print(stu["id"])
stu["email"]:"vinita@gmail.com"
print(stu)