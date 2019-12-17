with open("input.txt", "r") as infile:
    input = int(infile.read())
SIZE = 300
grid = [[0 for i in range(SIZE)] for j in range(SIZE)]

for row in range(SIZE):
    for col in range(SIZE):
        y = row+1
        x = col+1
        power = (((x+10)*y+input)*(x+10)//100)%10 - 5
        grid[row][col] = power
maxTotal = 0
(x, y, size) = (0, 0, 0)
sumgrid = [[0 for i in range(SIZE+1)] for j in range(SIZE+1)]
for row in range(1,SIZE+1):
    for col in range(1,SIZE+1):
            sumgrid[row][col] = sumgrid[row-1][col] + sumgrid[row][col-1] + grid[row-1][col-1] - sumgrid[row-1][col-1]
s = 3
for row in range(SIZE-s):
    for col in range(SIZE-s):
        total = sumgrid[row+s][col+s] - sumgrid[row][col+s] - sumgrid[row+s][col] + sumgrid[row][col]
        if(total > maxTotal):
            (x,y,size) = (col+1, row+1, s)
            maxTotal = total
print("{},{}".format(x,y))
for s in range(SIZE):
    for row in range(SIZE-s):
        for col in range(SIZE-s):
            total = sumgrid[row+s][col+s] - sumgrid[row][col+s] - sumgrid[row+s][col] + sumgrid[row][col]
            if(total > maxTotal):
                (x,y,size) = (col+1, row+1, s)
                maxTotal = total
print("{},{},{}".format(x,y,size))