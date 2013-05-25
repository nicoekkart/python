"""
Largest palindrome product
--------------------------
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Approach:

The biggest number you can make with two 3-digit numbers is 999*999 = 998001
So the highest palindrome has to be in the form abccba
This number can be written as 100000*a + 10000*b + 1000*c + 100*c + 10*b + a = 100001*a + 10010*b + 1100*c
100001*a + 10010*b + 1100*c = 11*(9091*a + 910*b + 100c*)
==> One of the numbers is divisible by 11 (because 11 is prime) ==> We'll start at 990 (divisible by 11) and decrement by 11 every time.
We'll have to check to 900, because it has to start with a 9, and 900*999=899100

## is palindrome function ##

Turn the number in a string, reverse it and check if it's equal to the original.
"""
def is_palindrome(n):
    return str(n)==str(n)[::-1]

palindromes = set()

for i in range(999,900,-1):
    for j in range(990,900,-11):
        if is_palindrome(i*j):
            palindromes.add(i*j)

print("The biggest palindrome is {0}".format(max(palindromes)))