# Lambda Functions - Anonymous(without name), small functions, single line functions
# lambda syntax:  lambda keyword
# lambda arguments : expression
#Types:
# 1) Lambda with one parameter
'''sq=lambda x:x*x
print(sq(5))'''

# 2) Lambda with multiple parameter
'''x1=5
x2=6
add=lambda x1,x2:x1+x2
print(add(x1,x2))'''

# 3) Lambda with if-else
'''check=lambda x: "Even" if x%2==0  else "Odd"
print(check(7))
print(check(8))'''

# when should we use lambda func?
# --> small functions temporarily,especially with:
# map()- It applies function to every element of an iterable, filter(), sorted(), reduce()
# synatax: map(function,iterable)
'''nums=[1,2,3,4,5]
sqs=list(map(lambda x:x*x,nums))
print(sqs)'''

# map without lambda
'''def sq(x):
    return x*x
nums=[1,2,3,4,5]
result=map(sq,nums)
print(list(result))'''

# filter() - It is used when we want to select only elements that satisfy a condition
# syntax: filter(function,iteration)
'''nums=[1,2,3,4,5]
result=filter(lambda x:x%2==0,nums)
print(list(result))'''

# reduce() - It repeatedly applies a function to elements and reduce entire sequence to one final value
'''from functools import reduce
nums=[1,2,3,4,5,6,7,8]
result=reduce(lambda a,b:a+b,nums)   a=1,b=2 result=3 then a=3,b=3 result=6,a=6,b=4,result=10
print(result)'''

# sorted() - to arrange the values
'''nums=[1,4,3,2]
result=sorted(nums)
print(result)'''

#values are arranged as per length of items
'''names=["vinita", "tungala","naidu"]
result=sorted(names,key=len)
print(result)'''

# abs means negative nums also converted into positive nums
'''nums=[1,-3,6,7,-4]
result=sorted(nums,key=abs)
print(result)'''

# sorting words by using last character
'''names=["vinita","indu","harshini","madhu"]
result=sorted(names,key=lambda x:x[-1])
print(result)'''


