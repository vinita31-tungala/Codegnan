oop=object oriented programming
#it is programming approach where we organize our program around objects rather than only functions 
#and variables

# student:
# data:
# -name,age,marks,roll_no
# -study(),attend_classes(),write_exam(),display_
#in oops ,we combine data+behavior into object 

#1.class
#-blueprint /template to create objects and it does not have memory allocation 

#2.objects:
#instances of classes 
#object -actual thing created from blueprint 

# class student:
#     pass
# student1=student() #student1->object
# student2=student()

#attributes
#attribute are the data/properties associated 
#with an object.

# class student:
#     pass
# student1=student() 
# student1.name="Rahul"
# student.age=23
# student.marks=95
# print(student1.name)
# print(student1.age)
# print(student1.marks)


#methods :
#methods -functions created inside the class

# class student1:
#     def study(self):
#         print("student is studying")
# student1.study()
# student1.study()
#methods only belongs to class

#constuctor-it is a special method which is automatically called when an object of class is created

#_init_()
# class student:
#         def_init_(self):
#         print("student is studying")
# student1=student()
# student1=student()
# student1=student()

#constructor is used to initialize the attributes of an object

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
# student1=student("mounika",20,95)
# print(student1.age)
# print(student1.age)
# print(student1.marks)

#self represents current object.

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name,self.age,self.marks)
# student1=student("mounika",20,95)
# student1.display()            

#encpsulation:
#encapsulation means bundling of data and methods together inside a class 
#and controlling how the data is accessed or modified.

# class BankAccount:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+=amount    
#     def withdraw(self,amount):
#         self.balance-=amount
#     def get_balance(self):
#         return self.balance
# ba=BankAccount(50000)
# ba.deposit(10000)
# ba.withdraw(5000)
# print(ba.get_balance())        

#double undersore indicates a private-like 
#attribute in python through name managing 

#getter and setter concept

#private data
#getter ->read data 
#setter ->modify data safely

# class student:
#     def __init__(self,marks):
#         self.__marks=marks
#     def get_marks(self):
#         return self.__marks
#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print("Invalid marks")
# student=student(80)
# print(student.get_marks())
# student.set_marks(90)
# print(student.get_marks())   
# 
# #inheritance:
# #process of acquring properties from parent to child class
# 
# types of inheritance
# #1.single inheritance
# one parent->one child
# class Animal:
#     def eat(self):
#       print("Animal is eating")
# #child class
# class Lion(Animal):
#     def roar(self):
#        print("Lion Roars")
# l=Lion() 
# l.eat()
# l.roar()
                 
# class Father:
#     def father_properties(self):
#         print("Father properties")
# class Mother:
#     def mother_properties(self):
#         print("Mother properties")  
# class Child(Father,Mother):
#     def child_properties(self):
#         print("Child properties")   
# c=Child()
# c.father_properties()
# c.mother_properties()
# c.child_properties()

#multi-level inheritance:
#inheritance happens across multiple levels
#Grandparent->parent->child
# class Grandparent:
#     def house(self):
#         print("grandparent's house")
# class parent(Grandparent):
#     def car(self):
#         print("parent's car")
# class child(parent):
#     def bike(self):
#         print("child's bike")   
# c=child()
# c.house()
# c.car()
# c.bike()                        

#hierachical inheritance:
#one parent->multiple children

# class Animal:
#     def eat(self):
#         print("Animal is eating")   
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")  
# class cat(Animal):
#     def meow(self):
#         print("cat meows")  

# class A:
#     def method_a(self):
#         print("A")
# class B:
#     def method_b(self):
#         print("B")
# class C(A):
#     def method_c(self):
#         print("C") 
# class D(B,C):
#     def method_d(self):
#         print("D")
# obj=D()
# obj.method_a()
# obj.method_b()
# obj.method_c()
# obj.method_d()        

#super method
#in python,super () is used to acess functionality 
#from the parent class

# class Parent:
#     def show(self):
#         print("Parent method")
# class Child(Parent):
#     def show(self):
#         super().show()
#         print("Child method")
# c=Child()
# c.show()

#super() with constructor 
# class person:
#     def __init__(self, name):
#         self.name = name
# class student(person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks
# s=student("Rahul", 95)
# print(s.name)
# print(s.marks) 
# 
# vehicle and car
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#     def start(self):
#         print(f"{self.brand} {self.model} is starting.")
#     def stop(self):
#         print(f"{self.brand} {self.model} is stopping.") 
# vehicle=Vehicle("Toyota", "Camry")
# vehicle.start()
# vehicle.stop()   

#person and student
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name,self.ag)
# class Student(Person):
#     def __init__(self,name,age, roll_no, course):   
#         super().__init__(name,age)
#         self.roll_no=roll_no
#         self.course = course
#     def displayy(self):     
#         print(self.name,self.age,self.roll_no,self.course)
# object=Student("Mounika",20,101,"CSE")
# object.displayy()