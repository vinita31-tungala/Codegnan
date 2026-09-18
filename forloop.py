# Loops: Doing the same task for the repetition of times
# 1) For loop 2) While loop
# For loop - We use when we know the no of iterations needs to perform
#Eg: Cooking food for a family

# By using index
'''for i in range(0,10):
#print("Hello Vinita")
    print(i)'''

'''nums=[10,20,30,40,50]
for i in range(0,5):
    print(nums[i])'''

# By using value
'''nums=[10,20,30,40,50]
for num in nums:
    print(num)'''

# Print even nums from 1 to 10
'''for i in range(1,10):
    if i%2==0:
        print(i)'''

# To reverse the nums from 10 to 1
'''for i in range(10,0,-1):
    print(i,end=" ")'''

# Sum of all nums upto 10
'''total=0
for i in range(1,11):
    total+=i
    print(total)'''

# Table of 5
'''num=5
for i in range(1,11):
    print(num*i)'''

# Finding Largest num without using max
nums=[1,2,3,4,5]
largest=nums[0]
for num in nums:
    if num>largest:
        largest=num
print(largest)

# # While loop - Whenever we don't know the no of iterations needs to perform
# Eg: Cooking food in restaurant
'''i=1
while i<=5:
    print(i,end=" ")
    i=i+1'''

# Print even nums from 1 to 10
'''nums=2
while nums<=10:                                      #if nums%2==0:
    print(nums)
    nums+=2'''
# Print odd nums from 1 to 10
'''nums=1
while nums<=10:
    print(nums)
    nums+=2'''

# To reverse the nums from 10 to 1
'''i=10
while i>=1:
    print(i)
    i=i-1'''


    

