"""
Largest product in a grid
-------------------------

In the 2020 grid below, four numbers along a diagonal line have been marked in red.
## Number can be found in 2020grid.txt ##
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 2020 grid?

Approach:

Read the grid in a 2-dimensional array.
Go trough each number and check four directions. (down,right,diagonal_down_right, diagonal_up_right) save it in a set
Get the max.
"""
g = []
for line in open('2020grid.txt'):
    line = line.rstrip("\n") #remove trailing \n
    g.append([int(i) for i in line.split()])

products = set()

for i in range(20):#vertical
    for j in range(20):#horizontal
        #right
        if j+3<20: products.add(g[i][j]*g[i][j+1]*g[i][j+2]*g[i][j+3])
        #down
        if i+3<20: products.add(g[i][j]*g[i+1][j]*g[i+2][j]*g[i+3][j])
        #diagonal down right
        if i+3<20 and j+3<20: products.add(g[i][j]*g[i+1][j+1]*g[i+2][j+2]*g[i+3][j+3])
        #diagonal up right
        if i-3>0 and j+3<20: products.add(g[i][j]*g[i-1][j+1]*g[i-2][j+2]*g[i-3][j+3])

answer = max(products)
print("The max product is {0}".format(answer))