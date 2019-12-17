from collections import deque

def getTurnOrder():
    aliveUnits = []
    for unitId, unit in enumerate(units):
        if(unit['health']>0):
            aliveUnits.append((unit['loc'], unitId))
    aliveUnits = sorted(aliveUnits)
    return list(map(lambda x: x[1], aliveUnits))

def otherType(type):
    return 'G' if type == 'E' else 'E'

dx = [0,-1,1,0]
dy = [-1,0,0,1]
for elfDamage in range(3,200):
    with open("input.txt") as infile:
        raw = list(map(list, infile.read().split("\n")))
    units = []
    width = len(raw[0])
    height=  len(raw)
    nE, nG = 0, 0
    oE = 0
    for (rowNo, row) in enumerate(raw):
        newRow = []
        for (colNo, cell) in enumerate(row):
            if cell == 'G':
                units.append({'type': 'G', 'loc': (rowNo, colNo), 'health': 200})
                nG += 1
            elif cell =='E':
                units.append({'type': 'E', 'loc': (rowNo, colNo), 'health': 200})
                nE += 1
                oE += 1

    turn = 0


    endGame = False
    while(True):
        #print("Turn {}".format(turn))
        #for row in raw:
        #    print(''.join(row))
        turnOrder = getTurnOrder()
        for id in turnOrder:
            unit = units[id]
            if(unit['health'] <= 0):
                continue
            if(nE == 0 or nG == 0):
                endGame = True
                break
            type, (curRow, curCol) = unit['type'], unit['loc']
            adjEnemy = False
            for i in range(4):
                newRow = curRow+dy[i]
                newCol = curCol+dx[i]
                if(raw[newRow][newCol] == otherType(type)):
                    adjEnemy = True
            nextMove = -1
            if(not adjEnemy):
                #Move
                visited = [[False for i in range(width)] for i in range(height)]
                q = deque()
                q.append(('', (curRow, curCol)))
                visited[curRow][curCol] = True
                foundPath = False
                while(q):
                    path, (qRow, qCol) = q.popleft()
                    for i in range(4):
                        npath = path
                        nRow = qRow+dy[i]
                        nCol = qCol+dx[i]
                        if(raw[nRow][nCol] == '.' and not visited[nRow][nCol]):
                            npath += str(i)
                            for j in range(4):
                                anRow = nRow+dy[j]
                                anCol = nCol+dx[j]
                                if(raw[anRow][anCol] == otherType(type)):
                                    foundPath = True
                                    nextMove = int(npath[0])
                                    break
                            visited[nRow][nCol] = True
                            q.append((npath, (nRow, nCol)))
                        if(foundPath):
                            break
                    if(foundPath):
                        break
                if(foundPath):
                    #print('{} at ({} {}) moves to ({} {})'.format(type, curRow, curCol, curRow + dy[nextMove], curCol + dx[nextMove]))
                    raw[curRow][curCol] = '.'
                    curRow += dy[nextMove]
                    curCol += dx[nextMove]
                    raw[curRow][curCol] = type
                    unit['loc'] = (curRow, curCol)
            enemyID = -1
            enemyHealth = 1E99
            for i in range(4):
                newRow = curRow+dy[i]
                newCol = curCol+dx[i]
                if(raw[newRow][newCol] == otherType(type)):
                    for (uID, unit) in enumerate(units):
                        if(unit['type'] == otherType(type) and unit['health'] < enemyHealth and unit['loc'][0] == newRow and unit['loc'][1] == newCol and unit['health'] > 0):
                            enemyID = uID
                            enemyHealth = unit['health']
                            break
            if(enemyID != -1):
                enemyUnit = units[enemyID]
                enemyUnit['health'] -= 3 if type == 'G' else elfDamage
                #print('{} at ({} {}) attacks unit at ({} {})'.format(type, curRow, curCol, enemyUnit['loc'][0], enemyUnit['loc'][1]))
                if(enemyUnit['health'] <= 0):
                    eRow, eCol = enemyUnit['loc']
                    if(otherType(type) == 'G'):
                        nG -= 1
                    else:
                        nE -= 1
                    raw[eRow][eCol] = '.'
                    #print('{} at {} {} dies'.format(enemyUnit['type'], enemyUnit['loc'][0], enemyUnit['loc'][1]))
        if(endGame):
            break
        turn += 1
    if(elfDamage == 3):
        part1 = 0
        for unit in units:
            if(unit['health'] > 0):
                part1 += unit['health']
        part1 *= turn
        print(part1)
    if(nE == oE):
        part2 = 0
        for unit in units:
            if(unit['health'] > 0):
                part2 += unit['health']
        part2 *= turn
        print(part2)
        break
    