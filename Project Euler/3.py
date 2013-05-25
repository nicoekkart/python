"""
Largest prime factor
--------------------

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?

Approach:

Prime factorization:

Start dividing the number by 2, increment the divisor every time.
If it divides evenly, add it to the prime_factors list and divide the number.
Stop when divisor*divisor>the number. 

Simply find the last (-1)
"""

def prime_factors(n):
    #inspired by http://stackoverflow.com/a/412942 (almost literally the same)
    d = 2
    factors = []
    while n>2:
        while n%d==0:
            factors.append(d)
            n/=d
        d += 1
        if d*d>n:
            if n>1: factors.append(n)
            break
    return factors

answer = prime_factors(600851475143)
print("The prime factors of 600851475143 are {0}. So the answer is {1}".format(answer,answer[-1]))