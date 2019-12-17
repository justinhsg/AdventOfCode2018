import queue
with open("test.txt", "r") as infile:
    inputs = infile.read().split("\n")
pots = inputs[0].split(" ")[2]

nextGen = {}
for i in inputs[2:]:
    [before, _, after] = i.split(" ")
    nextGen[before] = after

def nextGeneration(s, center):
    curMid = center
    news = '....'+s+'....'
    nexts = ''
    for i in range(2, len(news)-2):
        substr = news[i-2:i+3]
        nexts += nextGen[substr] #if substr in nextGen else '.'
    curMid = center+2
    trunc = 0
    while(nexts[trunc]=='.'):
        trunc += 1
    end = len(nexts)-1
    while(nexts[end]=='.'):
        end -= 1
    nexts = nexts[trunc:(end+1)]
    curMid -= trunc
    return (nexts, curMid)

generationCount = 0
curC, curPot = 0, pots
prevSum = 0
sum = 0
diff = 0
while (True):
    if(generationCount == 1000): break
    generationCount += 1;
    curPot, curC = nextGeneration(curPot, curC)
    sum = 0
    for (idx, pot) in enumerate(curPot):
        if(pot == '#'):
            sum += (idx - curC)
    if(generationCount == 20):
        print(sum)
    diff = sum - prevSum
    prevSum = sum
print((int)(5E10 - generationCount)*diff+sum)
