from functools import reduce
from collections import deque

with open("input.txt", "r") as infile:
    coords = list(map(lambda x: list(map(int, x.split(", "))), infile.read().split("\n")))

locs = [[(x[0], x[1])] for x in coords]


minx = reduce(lambda x, y: min(x, y[0]), coords, 1E99)
maxx = reduce(lambda x, y: max(x, y[0]), coords, -1)
miny = reduce(lambda x, y: min(x, y[1]), coords, 1E99)
maxy = reduce(lambda x, y: max(x, y[1]), coords, -1)
areas = [0 for i in range(len(coords))]
ignore = set()
def within(a,x,b):
    return x <= b and x >= a

for row in range(miny, maxy+1):
    for col in range(minx, maxx+1):
        minDist = 1E99
        closest = []
        for id, [xcoord, ycoord] in enumerate(coords):
            dist = abs(ycoord-row) + abs(xcoord-col)
            if(dist < minDist):
                closest = [id]
                minDist = dist
            elif (dist == minDist):
                closest.append(id)
        if(row == miny or row == maxy or col == minx or col == maxx):
            for i in closest:
                ignore.add(i)
        elif(len(closest)==1):
            areas[closest[0]] += 1
part1 = 0
for (id, count) in enumerate(areas):
    if(id in ignore):
        continue
    else:
        part1 = max(part1, count)
print(part1)

part2 = 0

for row in range(miny, maxy+1):
    for col in range(minx, maxx+1):
        acc = 0
        for [xcoord, ycoord] in coords:
            acc += abs(ycoord-row) + abs(xcoord-col)
            if(acc >= 10000):
                break
        if(acc < 10000):
            part2+=1
print(part2)
            