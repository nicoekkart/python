"""
Summation of primes
-------------------

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Approach:

The sieve of eratosthenes with a limit of 2-million is perfect for this.
"""
def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


answer = sum(primes_sieve(2000000))
print("The sum of all the primes bellow two million is {0}".format(answer))