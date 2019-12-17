with open("input.txt", "r") as infile:
    input = infile.read().strip().split("\n")
    
processed = []
maxX = 0
maxY = 0
for i in range(len(input)):
    tList = input[i].split();
    processed.append((int(tList[0][1:]), int(tList[2].split(",")[0]),int(tList[2].split(",")[1][:-1]),int(tList[3].split("x")[0]), int(tList[3].split("x")[1])))
    maxX = max(maxX, processed[i][1]+processed[i][3])
    maxY = max(maxY, processed[i][2]+processed[i][4])

    
fabric = [[0 for i in range(1000)] for i in range(1000)]

for i, val in enumerate(processed):
    for row in range(val[1], val[1]+val[3]):
        for col in range(val[2], val[2]+val[4]):
            fabric[row][col] += 1
p1 = 0
for i in range(1000):
    for j in range(1000):
        if(fabric[i][j]>1):
            p1+=1
print(p1)

for i, val in enumerate(processed):
    found = True
    for row in range(val[1], val[1]+val[3]):
        for col in range(val[2], val[2]+val[4]):
            if(fabric[row][col] > 1):
                found = False
                break
    if(found):
        print(val[0])
        break