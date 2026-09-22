# Scope - It is the region of a program where a variable can be accessed.
# 1. Local scope   2. Global scope
# Local Scope - A variable that created inside the function
'''def display():
    name="vinita"
    age=21
    print(name)
    print(age)
display()'''
# An error can be raised if want to print name outside the function like below line to display()
# Different functions can have variables with same name
'''def first():
    x=10
    print(x)
def second():
    x=20
    print(x)
first()
second()'''
# Global Scope - A variable that created outside the function
'''name="vinita"
age=21
def display():
    name="tungala"
    print(name)
    print(age)
display()
print(name)'''

x=10
'''def display():
    global x        # global keyword is used to remains the x=20 for both x
    x=20
#print(x)           ---> prints 10 
display()
print(x) '''    # prints 20
# No error is raised when we try to print the name outside the function,name can be print twice

# Pass by value and pass by reference
'''def display(x):
    x=20
a=10
display(a)
print(a)    #prints output as 10
'''

# Pass by value -  A copy of value is passed to the function,changes made inside the function and only copy value is changed
# Pass by reference - It changes both copy value and original value

#pass by value:
'''def change(x):                         a-->10
    x=20                                  #calling the function(a)
    print("Inside function:",x)           #x receives a reference to the same integer
a=10                                      #object
change(a)                                 #x=20
print("Outside function:",a)'''           #Before:
                                          #a->10  x=10
                                          #after x=20
                                          #a=10 , x=20

'''def add_10(x):
    x+=10
    print("Inside function:",x)
a=20
add_10(a)
print("Outside function:",a)'''

#pass by reference:

'''def add_element(data):
    data.append(40)
values=[10,20,30]          output: [10,20,30,40]
add_element(values)
print(values)'''

# Recursion - function calling iteself
'''def count_down(n):
    #Base case                output:5
    if n==0:                         4
        return                       3
    #recursive case                  2
    print(n)                         1
    count_down(n-1)
count_down(5)'''

#Factorial of a number using recursion
'''def fact(n):
    if n<=1:
        return 1
    #recursive case
    return n*fact(n-1)
print(fact(5))'''

# Fibonacci series using recursion
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n=5
for i in range(n):
    print(fib(i),end=" ")                                               