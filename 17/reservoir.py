from collections import deque

with open("input.txt", "r") as infile:
    raw = list(map(lambda x: x.split(", "), infile.read().split("\n")))
    
    
minx = 500
maxx = 500
maxy = 0
miny = 1E10
for [first, second] in raw:
    if(first[0] == 'x'):
        xval = int(first[2:])
        minx = min(minx, xval)
        maxx = max(maxx, xval)
        yleft, yright = list(map(int, second[2: ].split("..")))
        miny = min(miny, yleft, yright)
        maxy = max(maxy, yleft, yright)
    else:
        yval = int(first[2:])
        miny = min(miny, yval)
        maxy = max(maxy, yval)
        xleft, xright =  list(map(int, second[2: ].split("..")))
        maxx = max(maxx, xleft, xright)
        minx = min(minx, xleft, xright)
minx -=1
maxx += 1

res = [['.' for i in range(minx, maxx+1)] for i in range(maxy+1)]
res[0][500-minx] = '+'

for [first, second] in raw:
    if(first[0] == 'x'):
        xval = int(first[2:])
        yleft, yright = list(map(int, second[2: ].split("..")))
        for i in range(yleft, yright+1):
            res[i][xval-minx] = '#'
    else:
        yval = int(first[2:])
        xleft, xright =  list(map(int, second[2: ].split("..")))
        for i in range(xleft, xright+1):
            res[yval][i-minx] = '#'



    
res[1][500-minx] = '|'

st = deque()
drow = [0, 0, -1, 1, 0]
dcol = [-1, 1, 0, 0, 0]

for i in range(5):
    newRow = 1+drow[i]
    newCol = 500-minx+dcol[i]

    if(newRow >= 0 and newRow <= maxy and newCol >= 0 and newCol <= maxx-minx):
        if(res[newRow][newCol] == '.' or res[newRow][newCol] == '|'):
            st.append((newRow, newCol))
with open("map.txt", "w") as outfile:
    otext = ''
    for row in res:
        otext += ''.join(row) + '\n'
    outfile.write(otext)
while(st):
    (cRow, cCol) = st.pop()
    if(res[cRow][cCol] == '~'):
        continue
    aboveRow = (cRow-1)
    modified = False
    if(aboveRow >= 0):
        if(res[aboveRow][cCol] == '|' and res[cRow][cCol] == '.'):
            #print("Add | below")
            res[cRow][cCol] = '|'
            modified = True
        elif(res[aboveRow][cCol] == '~' and (res[cRow][cCol] == '.' or res[cRow][cCol] == '|')):
            #print("Add ~ below")
            res[cRow][cCol] = '~'
            modified = True
    leftCol = (cCol-1)
    if(leftCol >= 0):
        if(res[cRow][leftCol] == '~' and (res[cRow][cCol] == '.' or res[cRow][cCol] == '|')):
            #print("Add ~ right")
            res[cRow][cCol] = '~'
            modified = True
        elif(res[cRow][leftCol]=='|' and res[cRow][cCol] == '.'):
            if(cRow+1 <= maxy):
                if(res[cRow+1][leftCol] == '~' or res[cRow+1][leftCol] =='#'):
                    #print("Add | right")
                    res[cRow][cCol] = '|'
                    modified = True
                
    rightCol = (cCol+1)
    if(rightCol <= maxx-minx):
        if(res[cRow][rightCol] == '~' and (res[cRow][cCol] == '.' or res[cRow][cCol] == '|')):
            #print("Add ~ left")
            res[cRow][cCol] = '~'
            modified = True
        elif(res[cRow][rightCol]=='|' and res[cRow][cCol] == '.'):
            if(cRow+1 <= maxy):
                if(res[cRow+1][rightCol] == '~' or res[cRow+1][rightCol] =='#'):
                    #print("Add | left")
                    res[cRow][cCol] = '|'
                    modified = True
    belowRow = (cRow + 1)
    if(belowRow <= maxy):
        if(res[cRow][cCol] == '|'):
            tl, tr = cCol, cCol
            if(tl > 0):
                while(tl > 0 and res[cRow][tl] != '#'):
                    tl -= 1
            if(tr < maxx-minx):
                
                while(tr < maxx-minx and res[cRow][tr] != '#'):
                    tr += 1
            if(tl != 0 and tr != maxx-minx and tl != tr):
                #print(res[cRow][tl], res[cRow][tr])
                supported = True
                for i in range(tl, tr+1):
                    if(res[belowRow][i] != '#' and res[belowRow][i] != '~'):
                        supported = False
                        break
                if(supported):
                    #print("Add supported")
                    res[cRow][cCol] = '~'
                    modified = True
    if(modified):
        for i in range(5):
            newRow = cRow+drow[i]
            newCol = cCol+dcol[i]
            if(newRow >= 0 and newRow <= maxy and newCol >= 0 and newCol <= maxx-minx):
                if(res[newRow][newCol] == '.' or res[newRow][newCol] == '|'):
                    #print("Add {} {}".format(newRow, newCol))
                    st.append((newRow, newCol))
nFlow = 0
nStatic = 0
for row in range(miny,maxy+1):
    for col in range(maxx-minx):
        if(res[row][col]=='|'):
            nFlow += 1
        if(res[row][col]=='~'):
            nStatic += 1
print(nFlow + nStatic)
print(nStatic)

with open("map.txt", "w") as outfile:
    otext = ''
    for row in res:
        otext += ''.join(row) + '\n'
    outfile.write(otext)
