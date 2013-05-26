"""
Large sum
---------

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
## number can be found in `100numbers.txt` ##

Approach:

Python should be able to handle just summing them.
"""
answer = str(sum(int(i.rstrip('\n')) for i in open("100numbers.txt")))[:10]

print("The first ten digits are {0}".format(answer))