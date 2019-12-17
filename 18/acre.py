with open('input.txt') as infile:
    field = list(map(list, infile.read().split("\n")))

dcol = [-1,0,1,-1,1,-1,0,1]
drow = [-1,-1,-1,0,0,1,1,1]
def computeCell(row, col):
    nTree, nLumber = 0,0
    for i in range(8):
        nrow = row + drow[i]
        ncol = col + dcol[i]
        if(nrow >= 0 and nrow < len(field) and ncol >= 0 and ncol < len(field[0])):
            if(field[nrow][ncol]== '|'):
                nTree += 1
            if(field[nrow][ncol]== '#'):
                nLumber += 1
    if(field[row][col] == '.'):
        return '|' if nTree >= 3 else '.'
    if(field[row][col] == '|'):
        return '#' if nLumber >= 3 else '|'
    if(field[row][col] == '#'):
        return '#' if nTree >= 1 and nLumber >= 1 else '.'
        
        
def fieldtostr():
    return ''.join(map(lambda x: ''.join(x), field))
    
fields = []
fields.append(fieldtostr())
cycleStart,cycleEnd = 0, 1E99
for i in range(10000):
    newfield = []
    for rowNo, row in enumerate(field):
        newrow = []
        for colNo, cell in enumerate(row):
            newrow.append(computeCell(rowNo, colNo))
        newfield.append(newrow)
    field = newfield
    sfield = fieldtostr()
    if(sfield not in fields):
        fields.append(sfield)
    else:
        cycleEnd = i
        break
sfield = fieldtostr()
print(len(fields))
for gen, i in enumerate(fields):
    if i == sfield:
        cycleStart = gen
part1field = fields[10]
print(cycleStart, cycleEnd)
print(part1field.count("#")*part1field.count("|"))

part2field = fields[(1000000000 - cycleStart)%(cycleEnd+1-cycleStart) + cycleStart]
print((1000000000 - cycleStart)%(cycleEnd+1-cycleStart) + cycleStart)
print(part2field.count("#")*part2field.count("|"))
