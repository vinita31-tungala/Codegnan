#List - Ordered, Mutable,Allows different data types, Allows duplicates, Indexing and Negative Indexing, Slicing, Concatenation
#List Built-in functions - max(), min(), sorted(), len(), sum()
#Concatenation
'''a=["Vinita", "21", "Vekanuru"]
b=["Tungala",["Naidu"]]
print(b)
print(a+b)
c = [a[0]] + [b[0]] + a[1:] + [b[1]]
print(c)'''
#Repeation                             
'''d=[10,25]                           
print(d*2)'''
#Built-in functions
'''e=[1,2,3,4,5,3,4,8,3]
print(max(e))
print(min(e))
print(len(e))
print(sum(e))
print(sorted(e))'''  # data can be sorted by creating a new list,and then sort the elements
#List Methods
# append() - adds the value or item at the endind of the list
'''a=[1,2,3,4,5,3,4,8,3,3,3]
a.append(6)
print(a)
# extend() - adding multiple items to the list
a.extend([7,8])
print(a)
# pop() - deletes the last item
a.pop()
print(a)
# remove() - Specifies the particular item
a.remove(4)  # if list contains no duplicates then num can be directly deleted which we want to delete
print(a)
a.remove(3)  # if list contains duplicate values of element that we want to delete then first occurance of duplicate will be deleted
print(a)
# insert() - adding an element at a specific location
a.insert(2,11)
print(a)
# index() - returns the value using index nums
print(a.index(11))
# count() - counts the num that repeats
print(a.count(3))
# sort() - data can be sorted in already existing list(original list),means again no new list is created
a.sort()
print(a)
# reverse() - to reverse the list
a.reverse()
print(a)
print(a[::-1])
'''

a=4+8
print(a)
tup = (1, 2, 3, 4, 5)
print(tup[::-1])
one = "Coding"
two = "Chaf"
two=two[:3]+'e'+two[4:]
print(one + " " + two)

x=1
while x>0:
    print(x,end="")
    x+=1