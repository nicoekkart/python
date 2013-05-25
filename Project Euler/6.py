"""
Sum square difference
---------------------

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Approach:

No programming required
Sum of first n natural numbers = n(n+1)/2, so the square of that is (n**2(n+1)**2)/4.
Sum of first n natural numbers squared = n(n+1)(2n+1)/6

We need to have the difference ==> (n**2(n+1)**2)/4 - n(n+1)(2n+1)/6

In both cases n=100, so it becomes:

(100**2(101)**2)/4 - 100(101)(201)/6 = 25164150 = answer
"""

print("The difference between the sum of the squares of the first\
    one hundred natural numbers and the square of the sum is  {0}".format((100**2*(101)**2)/4 - 100*(101)*(201)/6))
