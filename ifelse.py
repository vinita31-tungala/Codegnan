#Conditional Statements - if,elif,else
#if - It executes the code when the condition is true only.
'''age=int(input())
if age>=18:
    print("Eligible for voting")'''
# if-else
'''if age>=21:
    print("Allowed for Alcohol")
else:
    print("Not permitted")'''
#elif - used when there is more than 2 conditions
'''marks=int(input())
if marks>=90:
    print("Grade-A")
elif marks>=80:
    print("Grade-B")
elif marks>=70:
    print("Grade-C")
elif marks>=60:
    print("Grade-D")
elif marks>=50:
    print("Grade-E")
else:
    print("Fail")'''
#Nested-if conditions
'''age=int(input())
has_id=True
if age>=21:
    print("Age Satisfied")
    if has_id:
        print("you can enter")'''
#Eg:ATM
'''Is this card valid?
Is this pin correct?
Is there enough balance?
Withdraw'''

'''card_valid=True
pin_correct=True
balance=4000
withdraw=5000
if card_valid:
    print("Card is valid")

    if pin_correct:
        print("Pin is correct")
   
        if withdraw <= balance:
            print("Enough balance")
            print("Withdraw successful")
        else:
            print("Insufficient balance")
    else:
        print("Enter correct pin")
else:
    print("Card is not valid")'''


#Online Shopping
'''Is the product available
Login with account
Is payment done'''

'''product_available=True
already_login=True
payment_done=False
if product_available:
    print("Product is available")
    if already_login:
        print("Continue payment")
        if payment_done:
            print("payment done successfully")
        else:
            print("Check again")
    else:
        print("Login to the account")
else:
    print("Not available")'''

#Problem-1 Num is positive or negative
'''num=int(input())
if num>0:
    print("Num is positive")
elif num<0:
    print("Num is negative")
else:
    print("Zero")'''

#Problem-2 Even or Odd
'''num=int(input())
if num%2==0:
    print("Num is even")
elif num%2!=0:
    print("Num is odd")
else:
    print("Zero")'''

#Problem-3 Largest of two nums
'''a=int(input("Enter first num:"))
b=int(input("Enter second num:"))
if a>b:
    print("First num is larger")
elif a<b:
    print("Second num is larger")
else:
    print("Both are equal")'''

#Problem-4 Admission in college
'''marks=int(input("Enter marks:"))
entrance=input("Did you pass entrance(yes/no):")
if marks>60 and entrance=="yes":
    print("Eligible for admission")
else:
    print("Not eligible")'''

#Problem-5 Login System
'''user_name=input("Enter username:")
password=input("Enter password:")
name="vinita"
pwd="123"
if user_name==name and password==pwd:
    print("Logged In")
else:
    print("Login Failed")'''

#Problem-6 Driving Eligibility
#Under 18 - Too young to drive
#18+ but no license - Valid license require
#18+ with license - You can drive
'''age=int(input("Enter age"))
license_valid=input("yes/no:")
if age>=18:
    if license_valid=="yes":
        print("You can drive")
    else:
        print("valid license required")
else:
    print("Too young to drive")'''

#Problem-7 Movie Ticket Pricing
#Below 5 - Free
#Between 5-12 - 100
#13 - 59 -200
#60 and above -120
'''age=int(input("Enter age:"))
if age<5:
    print("Ticket is free")
elif age>=5 and age<=12:
    print("Ticket price is 100")
elif age>=13 and age<=59:
    print("Ticket price is 200")
elif age>=60 :
    print("Ticket price is 120")'''

#Problem-8 Leap year  year divisible by 4 and 400 is leap year and not divisible by 100
'''year=int(input("Enter year:"))
if year%4==0:
    print("leap year")
    if year%400==0 and year%100!=0:
        print("leap year") 
else:
    print("Not a leap year")'''

#Problem-9  Employee Management System
#Performance>90 and Experience>5 = 20% hike
#Performance>90 and Experience<5 = 10% hike
#Performance>80 = 10% hike
#Performance>70 = 5% hike
'''performance=int(input("Enter performace percent:"))
experience=int(input("Enter years of experience:"))
if performance>90 and experience>5:
    print("20 percent hike")
elif performance>90 and experience<5:
    print("10 percent hike")
elif performance>80 and performance<90:
    print("10 percent hike")
elif performance>70 and performance<80:
    print("5 percent hike")'''

#password
#len=8, special char,nums,alphabets
password=input("Enter password:")
password_len=8
password_alpha=False
password_nums=True
password_spc=True
if password_len<8:
    print("Password should contain min 8 characters")
elif not password_alpha:
    print("Password should contain characters")
elif not password_nums:
    print("Password should contain atleast one num")
elif not password_spc:
    print("Password should contain atleast one special character")
else:
    print("Password saved")


