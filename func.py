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

'''def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(1,2,3,name="vinita",age=21)'''

# Even or Odd
'''def evenodd(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
print(evenodd(6))
print(evenodd(7))'''

# Return Largest of 3 nums
'''def num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("largest of three nums:",num(2,3,4))'''

'''def num(a,b,c):
    return max(a,b,c)
print("largest num:",num(2,3,5))'''

# Factorial of a num
'''def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
print(fact(5))'''

#Write a function that counts vowels in a string.
'''def count_vowels(s):
    count=0
    for ch in s.lower():
        if ch in "aeiou":
            count+=1
    return count
word="python programming"
print("num_of vowels:",count_vowels(word))'''

# Write a function that accepts any number of numbers and returns their average.
'''def avg(*args):
    return sum(args)/len(args)
print("average:",avg(10,20,30))'''

# Write a function that returns a new list containing only even numbers.
'''def even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = even_numbers(nums)

print(result)'''

# CHecking num is prime or not
'''def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))'''

#Reversing a string
'''def rev_string(s):
    return s[::-1]
print("reverse of string:",rev_string("python"))'''

#Check whether a string is a palindrome
'''def str_palin(s):
    return s==s[::-1]
print(str_palin("madam"))
print(str_palin("mom"))'''

# Remove duplicates from a list
'''def remove_duplicates(numbers):
    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result

print(remove_duplicates([1, 2, 2, 3, 4, 3, 5]))'''

# finding the second-largest number in a list
def second_largest(numbers):
    unique = list(set(numbers))

    if len(unique) < 2:
        return None

    unique.sort()
    return unique[-2]

print(second_largest([10, 20, 30, 40, 40]))