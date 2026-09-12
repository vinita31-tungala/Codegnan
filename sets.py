# Sets - unordered and stores unique elements, data can be stored in {}
'''a={10,20,30,40,10,20,50}
print(a)
b={}
print(type(b))
c=set()
print(type(c))
a.add(70)
print(a)'''
# Operations
# Union - Combining all the elements from the both sets and prints without duplicate values
print("Union")
a={10,20,30,40,10,20,50}
b={60,70,80,90,30}
print(a|b)
# Union using method()
print(a.union(b))
print("Intersection")
# Intersection - Prints only matched values from the both sets
print(a & b)
print(a.intersection(b))
print("Difference")
# Difference - Elements that exists in the first set but not in the second set
print(a-b)
print(b-a)
# Symmetric Difference - Elements that are in either set but not in both
print("Symmetric Difference ")
print(a^b)
# Methods - add(), len(), max(), min(), sum(), sorted(), update(), remove(), pop(), clear(), discard() 
print("Methods")
a.add(100)
print(a)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
c=sorted(a)
print(c)
a.update([90,80,77])
print(a)
a.remove((77))
print(a)
a.pop()
print(a)
b.clear()
print(b)
a.discard(100) 
print(a)

