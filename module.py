# Collections - Specialized data structures(Eg: List, Tuple, Set, Dictionary)
# import collections
#  ---> default dict - It allows us to provide a default value as zero

#searching a key which is not existed
'''from collections import defaultdict
students=defaultdict(int)
print(students["python"])'''

'''from collections import defaultdict
stu=defaultdict(list)
stu["CSD"].append("vinita")
stu["CSE"].append("indu")
stu["AIML"].append("bhavya")
print(stu)'''

#  ---> counter - Used to count how many an items appears  (representation : from collections import Counter)
# [1,2,3,2,1,4,3,3] - op: {"3":"3","1":"2","2":"2","4":"1"}
'''from collections import Counter
nums=[1,2,3,2,1,2,4,3,2,5]
count=Counter(nums)
print(count)'''

'''from collections import Counter
text="banana"
count=Counter(text)
print(count)'''

#  --->deque(Double-ended queue) - Used to delete the items from starting and ending as well.
'''from collections import deque
nums=deque([10,20,30])
nums.append(40)
print(nums)
# Add at beginning
nums.appendleft(5)
print(nums)
# Delete from last
nums.pop()
print(nums)
# Delete from beginning
nums.popleft()
print(nums)'''

#  --->namedtuple - A namedtuple is like a tuple whose values can also be accessed by using names.
'''from collections import namedtuple
Student=namedtuple("stu",["name","age","branch"])
stu=Student("vinita","21","CSD")
print(stu.name)
print(stu.age)
print(stu.branch)'''

# itertools
#count() - creates an infinte sequence
'''import itertools
nums=itertools.count(1)
print(next(nums))
print(next(nums))
print(next(nums))'''
#cycle() - repeats the values
'''import itertools
colors=itertools.cycle(["red","green","blue",])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))'''

# --->combinations - It select items where order does not matter
'''from itertools import combinations
nums=[1,2,3,4,5,6]
result=combinations(nums,2)
for item in result:
    print(item)'''

# --->permutations - It represents diffrent arrangements or orders
'''from itertools import permutations
nums=[1,2,3]
result=permutations(nums)
for item in result:
    print(item)'''

# chain() - combines multiple iterables into one sequence
'''from itertools import chain
a=[1,2,3]
b=[4,5,6]
result=chain(a,b)
for x in result:
    print(x)'''

# datetime module
# --->date
'''from datetime import date
today=date.today()
print(today)
print(today.year)
print(today.month)'''

# --->Time
# --->date+Time
'''from datetime import datetime
now=datetime.now()
print(now)'''

# finding specific date
'''from datetime import date
birthday=date(2004,10,31)
print(birthday)'''

#finding specific date and time
'''from datetime import datetime
dt=datetime(2026,9,26,15,35)
print(dt)'''

#timedelta - represents difference b/w date/time
'''from datetime import date,timedelta
today=date.today()
future=today+timedelta(days=10)
print(today)
print(future)'''

# date difference
'''from datetime import date
date1=date(2004,10,31)
date2=date(2026,9,25)
diff=date2-date1
print(diff)
print(diff.days)'''

# Formatting date - strftime()
'''from datetime import datetime
now=datetime.now()
formatted=now.strftime("%d-%m-%Y")
print(formatted)'''

'''from datetime import datetime
date_string="26-09-2026"
date_object=datetime.strptime(date_string,"%d-%m-%Y")
print(date_object)'''
# --->time differences
# --->formatting

# --->cartesian product
# --->grouping

# random
# random password generation - mainly works on random.choice() module
'''import random
chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789&%@#$!+_"
password=""
for  i in range(8):
    password+=random.choice(chars)
print("Password:",password)
'''

# Password Generator using string
'''import random
import string
chars=string.ascii_letters+string.digits+string.punctuation
password=""
for i in range(8):
    password+=random.choice(chars)
print("Password:",password)'''

# ATM Example
#if,elif,else,variables,input,Arithmetic operations,logical operations
# check pin
'''correct_pin=1234
pin=int(input("Enter pin:"))
if pin==correct_pin:
    print("Valid pin")
else:
    print("Pin Invalid,enter correctly")'''
# Add balance
'''balance=10000
deposit=5000
pin=int(input("Enter pin:"))
if pin==1234:
    balance+=deposit
    print(balance)
else:
    print("Invalid pin")'''
# Withdraw money
'''balance=10000
pin=int(input("Enter pin:"))
if pin==1234:
    amount=int(input("Enter withdraw amount:"))
    if amount<=balance:
        balance-=amount
        print("Withdraw successfull")
        print("Remaining balance:",balance)
    else:
        print("Insufficient balance")
else:
    print("Invalid pin")'''

# Complete ATM Example
'''balance=10000
pin=int(input("Enter pin:"))
if pin==1234:
    print("\n 1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Balance:",balance)
    elif choice==2:
        amount=int(input("Enter withdraw amount:"))
        if amount<=balance:
            balance-=amount
            print("withdraw successful")
            print("Remaining balance:",balance)
        else:
            print("Insufficient Balance")
    elif choice==3:
        amount=int(input("Enter amount:"))
        balance+=amount
        print("Deposit success")
        print("Updated balance:",balance)
    else:
        print("Invalid choice")
else:
    print("Invalid PIN,enter correctly")
'''