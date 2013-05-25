"""
Largest product in a series
---------------------------

Find the greatest product of five consecutive digits in the 1000-digit number.
## Number can be found in the file `longNumber.txt` ##

Approach:

Read the file and save it as a string.
Go trough each index (0..995) and save the product.
Get the max.

"""
def get_product(i, n):
    """helper function that gets the product, when the starting index and the number(str) is given."""
    return int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])

# Read the file
with open('longNumber.txt') as f:
    number = f.read()

answer = max(get_product(i,number) for i in range(0,995))

print("The maximum product of 5 consecutive digits in the number is {0}".format(answer))