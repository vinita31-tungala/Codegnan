'''name="vinita"
print(name)
a=name[2]
print(a)

word="python"
word[0]="j"
print(word) ''' #Sting is Immutable

#List
#Data Structure: Organizing data in a proper way like arranging the data in sequence order
# Mutable data,ordered data structure, allows duplicate values, allows indexing and slicing, allows heterogeneous data types,collection of items
#Data is Arranged in []
'''list1=[1,2,3,4,5]
print(list1)
print(list1[2])
list1[0]=9
print(list1)'''
'''student=[10,"vinita","avanigadda",5.2]
print(student)
print(type(list1))'''
#Addind elements to the list - using append() method - values can be added at the end of the list
'''list1.append(6)
print(list1)'''
#Extending the list - using extend() method - values can be added at the end of the list,to join 2 lists
'''list2=[7,8,9]
print(list2)
list1.extend(list2)
print(list1)'''
#Deleting the elements using pop()-deletes the last element of the list,remove()-deletes the specified element of the list,del()-deletes the specified index of the list
'''list1.pop()
print(list1)
list1.remove(9)
del list1[2]
print(list1)'''
#Concatenation of lists - using + operator
'''a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a+b)'''
#f.sting formatting - using f-string to format the string
'''name="vinita"
age=21
print(f"I am {name} and my age is {age}")'''
#f.formatting - using format() method to format the string
'''name="vinita"
age=21
print("I am {} and my age is {}".format(name,age))'''

#List Methods
'''append(x)
extend(iterable)
insert(i,x)
remove(x)
pop([i])
clear()
del list[i]
remove(x)
copy()
reverse()
sort(key=None,reverse=False)
count(x)'''
#append()
'''a=[1,2,3,4,5]
a.append(6)
print(a)
b=[6,7,8,9,10]
#extend()
a.extend(b)
print(a)
#insert()
a.insert(1,31)
print(a)
#remove()
print(a.remove(31))
#copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
#reverse()
b.reverse()
print(b)
#clear()
print(a.clear())'''
#Strings
'''name="vinita"
print(name[1:])
print(name[::-1])
print(name.upper())
print(name.lower())
print(len(name))
print(name.replace("v","V"))
print(name.count("i"))
print(sorted(name))'''

#Strings - Sequence of characters, ordered data structure, immutable data type, allows indexing and slicing, allows duplicate values, allows heterogeneous data types
#Data is arranged in "" or ''  eg: "vinita" or 'vinita'
'''place="I am from 'Vekanuru'" # or place='I am from "Vekanuru"'(String inside a string)
Place="I am from Vekanuru"
Loc='I am from Vekanuru'
print(Place==Loc)
print(place)
print(Loc)'''
#Indexing
a="vinita"
'''print(a[-1])
print(a[2])'''
#Slicing
'''print(a[2:4])
print(a[::-1])
print(a[3:])
print(a[:5])'''
#Want to miss the characters in between string  [start:stop:step]
#print(a[0:6:2])
'''print(a[-6:-1])
print(a[-6:-0]) #Zero is either positive or negative, but not both. It is always considered as positive. So, -0 is same as 0.
a="python"
result=a.replace("h","")
print(result)
print(a)
# or
text="python"
for char in text:
    if char=="h":
        continue
    print(char,end="")'''
#Concatenation of strings - using + operator
'''a="Vinita"
b="Tungala"
c=a+b
print(c)
print(a+ " " +b)'''
'''age=21
print(f"I am {age} ,years old")
print("I am", str(age), "years old")
#Membership in String
msg="python is case-sensitive"
print("java" in msg)'''
a="   Vinita  Tungala  "
print(a.upper())
print(a.isupper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.strip())
print(a)
print(a.find("Tungala"))
print(a.lstrip("Vinita"))
print(a.rstrip("Vinita"))
print(a.replace("Vinita","Raji"))
print(a.count("i"))
print(len(a))
print(a.startswith("hi"))
print(a.startswith("  "))
print(a.endswith("Tungala"))
print(a.startswith("a"))
print(a.split())
b=" ".join(a)
print(b)
#isalpha, #isdigit, isnum
e="1"
f="vinita"
g="001"
h="0.01"
i="-1"
j="9"
print(e.isalnum())
print(f.isalpha())
print(g.isdigit())
print(h.isdecimal())
print(i.isdecimal())
print(j.isdecimal())

