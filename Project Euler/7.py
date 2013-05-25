"""
10001st prime
-------------

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

Approach:

For this, we're going to use the Sieve of Eratosthenes, to get a list of prime numbers.
We'll need an upper bound for this. We need to get the 10001st prime, so 20 times bigger might be a good upper bound = 200000

"""
import itertools as it
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

counter = 1
for i in primes_sieve(200000):
    if counter==10001: break
    counter+=1

print("The 10001st prime is {0}".format(i))