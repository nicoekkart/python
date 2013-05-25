"""
Smallest multiple
-----------------

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Approach:

Prime factorization of 20..1:
20 = 2*2*5
19 = 19
18 = 3*3*2
17 = 17
16 = 2*2*2*
15 = 3*5
14 = 2*7
13 = 13
12 = 2*2*3
11 = 11
10 = 2*5
9  = 3*3
8  = 2*2*2
7  = 7
6  = 2*3
5  = 5
4  = 2*2
3  = 3
2  = 2
1  = 1

Now count needed number of primes (maximum used in a number) and multiply them together:

2*2*2*2*3*3*5*7*11*13*17*19 = 232792560 = answer
"""

print("The smallest number divisible by all of the numbers from 1 to 20 is {0}".format(2*2*2*2*3*3*5*7*11*13*17*19))