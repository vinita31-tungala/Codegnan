#Tuple
#Immutable data structure, ordered data structure, allows duplicate values, allows indexing and slicing, allows heterogeneous data types
#Data is Arranged in (),can store multiple data types
'''tuple1=(1,2,3,4,5)
print(tuple1)
print(tuple1[2])
tuple1[0]=9 #This will raise an error because tuples are immutable
print(tuple1)
tuple2=(10,"vinita","avanigadda",5.2)
print(tuple2)'''

#Set
#Mutable data structure, unordered data structure, does not allow duplicate values, allows indexing and slicing,data can be stored in {},can store multiple data types
'''set1={1,2,3,4,5,5,6,7,5,"Python","python"} #Python is case sensitive, so "Python" and "python" are considered different values
print(set1)'''

#Dictionary
#Mutable data structure, unordered data structure, does not allow duplicate keys, allows indexing and slicing
#data can be stored in {},can store multiple data types, key-value pairs
'''dict1={"name":"vinita","age":22,"city":"Hyderabad"}
print(dict1)
print(dict1["name"])
print(dict1["age"])
dict1["name"]="vini"
print(dict1)'''

#Type Conversions
#Converting one data type to another data type - eg:list to tuple or int to string
'''age=int(input("enter your age:")) # int()-integer,input()-string
print(age)
print(type(age))
print(str(age))
print(type(str(age)))
print(type(float(age)))'''
# Tuple
'''colors=("red","green","blue","orange","black")
me=("white","yellow")
print(colors)
print(colors[2])
print(colors+me)
# Methods
print(len(colors))'''
a=("1","2","3","4","5","3","2","6")
print(a)
print(a.count(5))
print(a[1:])
print(a*2)
print(max(a))
print(min(a))
b=list(a)
print(b)
print(b.append(7))
print(b.pop(6))
print(tuple(b))





