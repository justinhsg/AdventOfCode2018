from collections import deque

with open("in", 'r') as infile:
    line = infile.read()

    
def addpair(a,b):
    return (a[0]+b[0], a[1]+b[1])
    
regex = line[1:-1]

doors = dict()
checkpoints = deque([(0,0)])

dirs = dict()
dirs['N'] = (0,1)
dirs['E'] = (1,0)
dirs['S'] = (0,-1)
dirs['W'] = (-1,0)

doors[(0,0)] = set()

traverseStack = deque([(0, (0,0))])

states = set()
states.add((0, (0,0)))
while(len(traverseStack)!=0):
    (idx, pos) = traverseStack.pop()
    states.add((idx, pos))
    if(idx >= len(regex)):
        continue
    c = regex[idx]
    if(c in dirs):
        curPos = pos
        while(True):
            c = regex[idx]
            if(c not in dirs):
                break
            else:
                newPos = addpair(curPos, dirs[c])
                doors[curPos].add(newPos)
                if(newPos not in doors):
                    doors[newPos] = set()
                doors[newPos].add(curPos)
                curPos = newPos
                idx += 1
                if(idx >= len(regex)):
                    break
        if((idx, curPos) not in states):
            states.add((idx, curPos))
            traverseStack.append((idx, curPos))
    elif(c == '('):
        if((idx+1, pos) not in states):
            states.add((idx+1, pos))
            traverseStack.append((idx+1, pos))
        depth = 0
        while(True):
            idx+=1
            d = regex[idx]
            if(d == '('):
                depth += 1
            elif(d == '|' and depth == 0):
                if((idx+1, pos) not in states):
                    states.add((idx+1, pos))
                    traverseStack.append((idx+1, pos))
            elif(d == ')'):
                if(depth == 0):
                    break
                else:
                    depth -= 1
    elif(c == '|'):
        depth = 0
        while(True):
            idx+=1
            d = regex[idx]
            if(d == '('):
                depth += 1
            if(d == ')'):
                if(depth == 0):
                    if((idx+1, pos) not in states):
                        states.add((idx+1, pos))
                        traverseStack.append((idx+1, pos))
                    break
                else:
                    depth-=1
    elif(c == ')'):
        if((idx+1,pos) not in states):
            states.add((idx+1, pos))
            traverseStack.append((idx+1, pos))
visited = set()
visited.add((0,0))
bfsQueue = deque([((0,0), 0)])
nFarRooms = 0
maxDist = 0
while(len(bfsQueue)):
    pos, dist = bfsQueue.popleft()
    maxDist = max(maxDist, dist)
    for nextPos in doors[pos]:
        if(nextPos not in visited):
            visited.add(nextPos)
            if(dist+1 >= 1000):
                nFarRooms+=1
            bfsQueue.append((nextPos, dist+1))
print(maxDist)
print(nFarRooms)
                   