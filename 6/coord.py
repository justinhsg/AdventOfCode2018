from functools import reduce
from collections import deque

with open("input.txt", "r") as infile:
    coords = list(map(lambda x: list(map(int, x.split(", "))), infile.read().split("\n")))

locs = [[(x[0], x[1])] for x in coords]


minx = reduce(lambda x, y: min(x, y[0]), coords, 1E99)
maxx = reduce(lambda x, y: max(x, y[0]), coords, -1)
miny = reduce(lambda x, y: min(x, y[1]), coords, 1E99)
maxy = reduce(lambda x, y: max(x, y[1]), coords, -1)

map = [[[(-1) for i in range(maxx+1)] for j in range(maxy+1)] for k in range(len(locs))]

def within(a,x,b):
    return x <= b and x >= a

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for id in range(len(coords)):
#for id in range(1):
    q = deque()
    q.append(locs[id][0])
    map[id][locs[id][0][1]][locs[id][0][0]] = 0
    while(q):
        (curX, curY) = q.popleft()
        curD = map[id][curY][curX]
        for i in range(4):
            newX = curX+dx[i]
            newY = curY+dy[i]
            if(within(minx, newX, maxx) and within(miny, newY, maxy)):
                if(map[id][newY][newX] == -1):
                    map[id][newY][newX] = curD+1
                    q.append((newX, newY))

territories = [['.' for i in range(maxx+1)] for j in range(maxy+1)]
size = [0 for i in range(len(coords))]
infinites = set()
for row in range(len(map[0])):
    for col in range(len(map[0][row])):
        owners = []
        maxLength = 1E99
        for i in range(len(coords)):
            curLength = map[i][row][col]
            if(curLength < maxLength):
                owners = [i]
                maxLength = curLength
            elif (curLength == maxLength):
                owners.append(i)
        if(len(owners)==1):
            territories[row][col] = str(owners[0])
            size[owners[0]] += 1
            if(row == miny or row == maxy or col == miny or col == maxy):
                infinites.add(owners[0])
maxArea = 0

for i in range(len(coords)):
    if i in infinites:
        continue
    else:
        maxArea = max(maxArea, size[i])
part1 = maxArea