# Patterns
# Right-angled triangle from 1 to 6
'''for i in range(1,6):           
    for j in range(i):
        print("*",end="")
    print()'''

# Reversing the pattern from 5 to 1
'''for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()'''

# 5*5 Square pattern
'''for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()'''

# Rectangle
'''for i in range(3):         #rows=int(input("enter no of rows"))
    for j in range(5):        #cols=int(input("enter no of cols"))
        print("*",end=" ")    #for i in range(rows):
    print()'''                    #for j in range(cols):
                                     #print("*",end=" ")
                                #print()
# left-angled triangle pattern
'''n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()'''

# Triangle
'''n=5
for i in range(1,n+1):
    for j in range(n-i):
        print("",end="")
    for j in range(i):
        print("*",end=" ")
    print()'''

# Pyramid
'''n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):   # or (1,2*i)
        print("*",end="")
    print()'''

# Number system in right-angled triangle        #1
'''for i in range(1,6):                         #12
    for j in range(1,i+1):                      #123
        print(j,end=" ")                        #1234
    print()'''                                  #12345

'''for i in range(1,6):                #1
    for j in range(1,i+1):             #22
        print(i,end=" ")               #333
    print()  '''                       #4444

'''for i in range(1,6):                 #5
    for j in range(5,5-i,-1):           #54
        print(j,end=" ")                #543
    print()    '''                      #5432
                                        #54321

'''n=1                             
                                   #1
for i in range(1,5):               #2 3
    for j in range(i):             #4 5 6
        print(n,end=" ")           #7 8 9 10
        n+=1
    print()'''

'''for i in range(5):           #5 4 3 2 1
    for j in range(5,0,-1):     #5 4 3 2 1
        print(j,end=" ")        #5 4 3 2 1
    print()'''                  #5 4 3 2 1
                                #5 4 3 2 1


'''for i in range(5,0,-1):           #5 4 3 2 1
    for j in range(5,5-i,-1):        #5 4 3 2
        print(j,end=" ")             #5 4 3
    print()'''                       #5 4
                                     #5

'''for i in range(1,6):           #1
    for j in range(i,0,-1):       #2 1
        print(j,end=" ")          #3 2 1
    print()'''                    #4 3 2 1
                                  #5 4 3 2 1

# Numbers Pyramid
'''n=5                                1
for i in range(1,n+1):               123
    for j in range(n-i):            12345
        print(" ",end="")          1234567
    for j in range(1,2*i):        123456789
        print(j,end="")
    print()  '''

'''n=5                              1
for i in range(1,n+1):             222
    for j in range(n-i):          33333
        print(" ",end="")        4444444
    for j in range(0,2*i-1):    555555555
        print(i,end="")
    print()'''

'''n=5                               *********
for i in range(5,0,-1):               *******
    for j in range(n-i):               *****
        print(" ",end="")               ***
    for j in range(1,2*i):               *
        print("*",end="")
    print()'''

# Upper Pyramid
'''n=int(input("enter num of rows:"))              *
for i in range(1,n+1):                            ***
    for j in range(n-i):                         *****
        print(" ",end="")                       *******
    for j in range(1,2*i):                     *********
        print("*",end="")                       *******
    print()                                      *****
# Lower Pyramid                                   ***
for i in range(n-1,0,-1):                          *
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()'''

# Name Pattern
'''name="code"                              c
for i in range(1,len(name)+1):              co
    for j in range(i):                      cod
        print(name[j],end="")               code
    print()'''


'''name="code"                              c
for i in range(1,len(name)+1):              cc
    for j in range(i):                      ccc
        print(name[0],end="")               cccc
    print()'''


'''name="code"                              c
for i in range(0,len(name)):                oo
    for j in range(i+1):                    ddd
        print(name[i],end="")               eeee
    print()'''

n=5
for i in range(1,n+1):
    # Spaces before the pyramid
    for j in range(n-i):
        print(" ",end="")
        # Spaces b/w the stars
    for j in range(1,2*i):
        if i==n:
            print("*",end="")
        elif j==1 or j==2 * i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()