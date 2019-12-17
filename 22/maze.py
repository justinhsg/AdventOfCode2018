import heapq

with open("in", "r") as infile:
    lines = infile.read().split("\n")


depth = int(lines[0].split(" ")[1])
(targetX, targetY) = map(int,(lines[1].split(" ")[1]).split(","))

caveWidth=targetX+25
caveHeight=targetY+25
#984
gIdx = [[0 for _ in range(caveWidth)] for _ in range(caveHeight)]
eLevel = [[0 for _ in range(caveWidth)] for _ in range(caveHeight)]
for y in range(caveHeight):
    gIdx[y][0] = 48271*y
    eLevel[y][0] = (48271*y+depth)%20183
for x in range(caveWidth):
    gIdx[0][x] = 16807*x
    eLevel[0][x] = (16807*x+depth)%20183
    

    
    
for y in range(1, caveHeight):
    for x in range(1, caveWidth):
        eLevel[y][x] = (eLevel[y-1][x] * eLevel[y][x-1] + depth)%20183

eLevel[targetY][targetX] = depth%20183
    
rType = [[eLevel[y][x]%3 for x in range(caveWidth)] for y in range(caveHeight)]
typeConv = ['.','=','|']
vis = [[typeConv[rType[y][x]] for x in range(caveWidth)] for y in range(caveHeight)]

    
part1 = 0
for y in range(targetY+1):
    for x in range(targetX+1):
        part1+=rType[y][x]
print(part1)

#torch = 0, gear = 1, neither = 2
times = [[[1e100 for _ in range(caveWidth)] for _ in range(caveHeight)] for _ in range(3)]
times[0][0][0] = 0

pq = []
heapq.heappush(pq,(0, 0, 0, 0))
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

while(len(pq)!=0):
    time, tool, x, y  = heapq.heappop(pq)
    if(tool == 0 and x == targetX and y == targetY):
        print(time)
        #1018 too high
        break
    
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        possible = False
        if(newX>= 0 and newX < caveWidth and newY >= 0 and newY < caveHeight):
            newType = rType[newY][newX]
            if(tool == 0):
                if(newType == 0 or newType == 2):
                    possible = True
            if(tool == 1):
                if(newType == 0 or newType == 1):
                    possible = True
            if(tool == 2):
                if(newType == 1 or newType == 2):
                    possible = True
        if(possible):
            if(times[tool][newY][newX] > time+1):
                times[tool][newY][newX] = time+1
                heapq.heappush(pq, (time+1, tool, newX, newY))
    curType = rType[y][x]
    if(curType == 0):
        if(tool == 0):
            newTool = 1
        elif(tool == 1):
            newTool = 0
        else:
            print("ERROR")
            break
    elif(curType == 1):
        if(tool == 1):
            newTool = 2
        elif(tool == 2):
            newTool = 1
        else:
            print("ERROR")
            break
    elif(curType == 2):
        if(tool == 0):
            newTool = 2
        elif(tool == 2):
            newTool = 0
        else:
            print("ERROR")
            break
    if(times[newTool][y][x] > time+7):
        times[newTool][y][x] = time+7
        heapq.heappush(pq, (time+7, newTool, x, y))

