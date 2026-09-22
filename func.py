# Functions - A Block of code to do particular task
# Mainly used to avoid repition of code 
# Function keyword - def func_name(parameters):  
                        #function body

# Function creation
'''def greet():    #greet() - func_name
    #function body
    print("Hi")          #or return "Hello"
# Function calling      
greet()                 #print(greet())'''

# User-defined functions - User created functions like greet()
# Types of functions
#Type-1: No parameters, no return value
'''def greet():
    print("Hello")
greet()'''

#Type-2: parameters, but not return value
'''def greet(name):
    print("hello",name)
greet("Vinita")'''

#Type-3: No parameters,but return value
'''def greet():
    return "Vinita"
print(greet())'''

'''def num():
    return 100
result=num()
print(result)'''

#Type-4 Parameters and return value
'''def add(a,b):    # a,b - parameters
    return a+b                                  #or return a+b 
print(add(1,2))     # 1,2 - arguments           #result=add(1,2)
                                                #print(result)
                                              '''
# Returning multiple values
'''def calc(a,b):
    add=a+b
    sub=a-b
    return add,sub
x,y=calc(7,6)
print(x)
print(y)'''

# Positional Arguments - Arguments are matched based on their position, Order is Imp - Keyword arguments
'''def student(name,age):
    print("name",name)
    print("age",age)
student("Vinita",21)'''

# Keyword Arguments
'''def student(name,age):
    print(name)
    print(age)
student(age=21,name="vinita")'''

# Default Arguments
'''def greet(name="vinita"):
    print("hi",name)
greet("code")'''

# Variable - Length Arguments(*args)
# *args - It collects multiple positional arguments into a tuple
'''def add(*nums):
    total=0
    for number in nums:
        total+=number
    return total
print(add(10,20))
print(add(1,2,3,4,5,6,7,8,9,10))'''

# **kwargs - Keyword variable-length arguments --> It accepts multiple keyword arguments
# Output is printed in dictionary format
'''def stu_details(**details):
    print(details)
stu_details(
name="Vinita",
age="21",
city="Avanigadda")'''

def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(1,2,3,name="vinita",age=21)
