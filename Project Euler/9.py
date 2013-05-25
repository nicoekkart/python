"""
Special Pythagorean triplet
---------------------------

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Approach:

a+b+c = 1000 <=> c = 1000-a-b <=> c^2 = a^2 - 2000a + 2ab + b^2 - 2000b + 1000000
a^2 + b^2 = a^2 - 2000a + 2ab + b^2 - 2000b + 1000000
Solve for a and you get:

a = 1000*(b-500)/(b-1000)

Find a number b => a is an integer
"""
def yields_integer(b):
    a = (1000.*(b-500.))/(b-1000.)
    return a==int(a)

def get_a(b):
    return (1000.*(b-500.))/(b-1000.)

for i in range(1,1000):
    if yields_integer(i):
        a = get_a(i)
        c = (a**2+i**2)**.5
        print("a = {0}; b = {1}; c = {2}; abc = {3}".format(a,i,c,a*i*c))
        break