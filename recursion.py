#Find the factorial of a number
'''def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))'''

#Find the sum of numbers from 1 to n
'''def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))'''

#Print numbers from 1 to n
'''def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)'''

#Print numbers from n to 1
'''def print_reverse(n):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)

print_reverse(5)'''

#Calculate a number raised to a power
'''def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 4))'''

#Find the sum of digits of a number
'''def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))'''

#Reverse a number
'''def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

print(reverse_number(1234))'''

#Check whether a number is a palindrome
'''def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

def is_palindrome(n):
    return n >= 0 and n == reverse_number(n)

print(is_palindrome(121))
print(is_palindrome(123))'''

#Count the digits of a number
'''def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(54321))'''

#Find the greatest common divisor (GCD)
'''def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(24, 36))'''  #output:12
