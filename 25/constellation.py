with open ("in", "r") as infile:
    lines = infile.read().split("\n")

coords = [tuple(map(int, line.split(","))) for line in lines]

def manDist(a ,b):
    dist = 0
    for i in range(len(a)):
        dist += abs(a[i] - b[i])
    return dist
    
    
conId = 0
cons = dict()
for coord in coords:
    matched = []
    for id in cons:
        for star in cons[id]:
            if(manDist(coord, star) <= 3):
                matched.append(id)
                break
    if(len(matched) == 0):
        cons[conId] = set([coord])
        conId+=1
    else:
        
        for id in range(1,len(matched)):
            cons[matched[0]] |= cons[matched[id]]
            cons.pop(matched[id])
        cons[matched[0]].add(coord)
print(len(cons))