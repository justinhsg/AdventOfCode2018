with open("input.txt", "r") as infile:
    numbers = list(map(int,infile.read().split(" ")))

def getMetadata (nodeStartIdx):
    accTotal = 0
    nChildren = numbers[nodeStartIdx]
    nMeta = numbers[nodeStartIdx+1]
    ptrloc = nodeStartIdx+2
    for i in range(nChildren):
        (childLength, childAccTotal) = getMetadata(ptrloc)
        accTotal += childAccTotal
        ptrloc += childLength
    for i in range(nMeta):
        accTotal += numbers[ptrloc]
        ptrloc += 1
    return (ptrloc - nodeStartIdx, accTotal)

print(getMetadata(0)[1])

def getNewMetadata(nodeStartIdx):
    accTotal = 0
    nChildren = numbers[nodeStartIdx]
    nMeta = numbers[nodeStartIdx+1]
    ptrloc = nodeStartIdx+2
    childVals = []
    for i in range(nChildren):
        (childLength, childAccTotal) = getNewMetadata(ptrloc)
        childVals.append(childAccTotal)
        ptrloc += childLength
    if(nChildren == 0):
        for i in range(nMeta):
            accTotal += numbers[ptrloc]
            ptrloc += 1
    else:
        for i in range(nMeta):
            idx = numbers[ptrloc]
            if idx <= len(childVals):
                accTotal += childVals[numbers[ptrloc]-1]
            ptrloc += 1
    return (ptrloc - nodeStartIdx, accTotal)

print(getNewMetadata(0)[1])