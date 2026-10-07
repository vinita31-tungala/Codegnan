# Regular Expression - It is a pattern used to search,match,extract or validate text.
#re.search() - It searches for a pattern in a string and returns the first occurrence of the pattern.
#string
'''import re
text="Hi Vinita, How are you?"
result=re.search("Hi",text)
print(result)'''
# We need to use search() method when we want to know as to whether a pattern is present in a string or not. It returns a match object if the pattern is found, otherwise it returns None.

#re.match() - It checks for a match only at the beginning of the string.
'''import re
text="Hi Vinita, How are you?"
result=re.match("Hi",text)
print(result)'''

#re.fullmatch() - It requires entire string to match the pattern.
'''import re
text="Hi Vinita"
result=re.fullmatch("Hi Vinita",text)
print(result)'''

#re.findall() - It returns a list of all occurrences of the pattern in the string.
#\d - digits(from 0 to 9)
 #\d+ means one or more digits
'''import re
text="I have 10 apples and 20 oranges."
result=re.findall("\d+",text)   
print(result)'''

#\w - word characters (letters, digits, or underscores)
#\w+ means one or more word characters
'''import re
text="I have 10 apples and 20 oranges."
result=re.findall("\w+",text)
print(result)'''

# ^ - matches the start of the string
'''import re
pattern="^Hello"
print(re.search(pattern,"Hello World"))'''  # Match

# $ - matches the end of the string
'''import re
pattern="World$"
print(re.search(pattern,"Hello World")) ''' # Match

# r"^\d{4}$"
# Quantifiers - It tells regex how many times to match a character or group of characters.
# # *,+,?,{}
# * - matches 0 or more occurrences of the preceding character or group
# r "ab*" - matches "a", "ab", "abb", "abbb", etc.
# Because the * quantifier allows for zero occurrences, it will also match "a" without any "b"s following it.

# + - matches 1 or more occurrences of the preceding character or group
# r "ab+" - matches "ab", "abb", "abbb", etc., but not "a" alone.
# a is not valid here because the + quantifier requires at least one occurrence of "b" after "a".

# ? - matches 0 or 1 occurrence of the preceding character or group
# r "ab?" - matches "a" or "ab", but not "abb" or "abbb".
# r"colou?r" - matches "color" or "colour", but not "colouur" or "colr".

# {} - matches a specific number of occurrences of the preceding character or group
# r "a{4}" - matches "aaaa" but not "aaa" or "aaaaa".
#1234(correct), 123(corr), 12345(incorrect)
# r"^\d{4,6}$" - matches a string that contains between 4 and 6 digits are valid, but not less than 4 or more than 6 digits.

'''import re
value=input("Enter a number:")
pattern=r"^\d+$"
if re.fullmatch(pattern, value):
    print("only digits")
else:
    print("Invalid")'''

# Phno pattern valid or not
'''import re
phn=input("Enter num:")
pattern=r"^[6-9]\d{9}$"
if re.fullmatch(pattern,phn):
    print("Valid")
else:
    print("Invalid")'''

# E-mail pattern valid or not   -  username@domain.com
# r"^[\w.-]+@[\w.-]+\.\w+$"
# [\w.-]+  - username
# [\w.-]+  -domain
'''import re
email=input("Enter email:")
pattern=r"^[\w.-]+@[\w.-]+\.\w+$"
if re.fullmatch(pattern,email):
    print("Valid")
else:
    print("Invalid")'''

# Password pattern valid or not
import re
name=input("Enter name:")
password=input("Enter password:")
#Name
if re.fullmatch(r"[A-Z][a-z]+",name):
    print("Valid name")
else:
    print("Invalid name")
# r - raw string
# ^ - start of the string
# ?=. - positive lookahead assertion(It checks whether a certain pattern exists in the string without removing any characters.)
# * - zero or more occurrences of the preceding character or group
# [A-Z] - at least one uppercase letter
# ?=.*[a-z] - it checks password contains at least one lowercase letter

pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*\d).{8,}$"
#Password
if re.fullmatch(pattern,password):
    print("Valid password")
else:
    print("Invalid password")
