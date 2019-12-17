from queue import PriorityQueue
with open("input.txt", "r") as infile:
    comm = infile.read().split("\n")

    
reqs = dict();
processes = set()
for i in comm:
    splits = i.split(" ")
    req = splits[1]
    next = splits[7]
    processes.add(req)
    processes.add(next)
    if next not in reqs:
        reqs[next] = []
    reqs[next].append(req)
    
order = ''
for letter in processes:
    if(letter not in reqs):
        reqs[letter] = []


def isClear(letter):
    op = True
    for i in reqs[letter]:
        if i not in order:
            op = False
            break
    return op

while(len(order) != len(processes)):
    for i in range(26):
        letter = chr(i + ord('A'))
        if(isClear(letter) and letter not in order):
            order += letter
            break
print(order)

nIdle = 5
curPos = 0
donePos = -1
accTime = 0
pq = PriorityQueue()
done = dict()
inpro = dict()
for i in order:
    done[i] = False
    inpro[i] = False

def isReady(letter):
    if letter == '': return False
    op = True
    for i in reqs[letter]:
        if(not done[i]):
            op = False
            break
    return op

def allDone():
    for i in done:
        if(not done[i]):
            return False
    return True
    
while(not allDone()):
    
    if(curPos == len(order)):
        if(not pq.empty()):
            (newTime, doneLetter) = pq.get(block = False)
            done[doneLetter] = True
            accTime = newTime
            nIdle += 1
        continue
    else:
        nextLetter = ''
        for i in range(26):
            tLetter = chr(ord('A')+i)
            if(tLetter in processes):
                if(isReady(tLetter) and not done[tLetter] and not inpro[tLetter]):
                    nextLetter = tLetter
                    break
        if(isReady(nextLetter) and nIdle > 0):
            pq.put((accTime + ord(nextLetter)-ord('A')+1+60, nextLetter))
            inpro[tLetter] = True
            nIdle -= 1
            curPos += 1
            continue
        else:
            if(not pq.empty()):
                (newTime, doneLetter) = pq.get(block = False)
                done[doneLetter] = True
                accTime = newTime
                nIdle += 1
            continue
print(accTime)
    
    