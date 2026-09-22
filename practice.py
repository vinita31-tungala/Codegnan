# Reversing name using for loop
'''name="vinita"
reverse=""
for i in name:
    reverse=i+reverse
print(reverse)'''

#Reversing name using list index
'''name="vinita"
reversed_name=name[::-1]
print(reversed_name)'''

#1)Employee Performance Evaluation
'''name=input("Enter employee name:")
projects=int(input("No of projects completed:"))
rating=float(input("Performance rating:"))
Employee={"name":name,"projects":projects,"rating":rating}
if Employee["rating"]>=4 and Employee["projects"]>=5:
    status="Excellent"
elif Employee["rating"]>=3 and Employee["projects"]>=3:
    status="Good"
elif Employee["rating"]>=2:
    status="Needs Improvement"
else:
    status="Poor"
print(f"Employee status for,{Employee['name']}:{status}")'''

# 2) Number Classification
'''num=int(input("Enter num::"))
if num>0 and num%2==0:
    print("num is positive and even")
elif num>0 and num%2!=0:
    print("num is positive and odd")
elif num<0 and num%2==0:
    print("num is negative and even")
elif num<0 and num%2!=0:
    print("num is negative and odd")
else:
    print("Zero")'''

# 3) Shopping Discount
'''price=int(input("Enter price of product:"))
member=input("Is the customer a member?(yes/no):")
is_member=member=='yes'
if price>=10000 and member:
    Discount=20
elif price>=10000 and member:
    Discount=20
elif price>=5000 and member:
    Discount=10
elif price>=5000 and member:
    Discount=15
elif price<5000:
    Discount=0
discount_amount=price*(Discount/100)
final_price=price-Discount
print(f"final price is,{final_price}")'''

# 4) List Element Validation
'''numbers=[]
for i in range(5):
    num=int(input(f"enter 5 integers{i+1}:"))
    numbers.append(num)
if 50 in numbers:
    print("50 is available")
else:
    print("50 is not available")
positive_count=0
for num in numbers:
    if num>0:
        positive_count=positive_count+1
if positive_count>3:
    print("Many Positive numbers")'''

# 5) ATM Withdrawal Validation
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

# 6)Complex Student Scholarship
stu_age=int(input("Enter age:"))
percentage=int(input("Enter percentage:"))
family_income=int(input("Enter family income:"))
attendance=int(input("Enter attendance:"))
sports_part=input("Participation in sports?(yes/no)")
backlogs=int(input("Enter no of backlogs:"))
print("student qualifies for the scholarship")
if percentage >= 85 and attendance >= 90 and family_income <= 500000 and backlogs == 0:
    print("student qualifies for the scholarship")
if stu_age<18 and stu_age>25:
    if family_income>800000 and backlogs>2:
        print("rejected")


