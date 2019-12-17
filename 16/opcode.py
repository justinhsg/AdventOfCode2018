with open("input.txt", "r") as infile:
    #converts input to array of strings
    raw = infile.read()

firstpart, secondpart= raw.split("\n\n\n\n")
instructions = list(map(lambda x: x.split("\n"), firstpart.split("\n\n")))
pInst = []
for i in instructions:
    before = list(map(int , i[0][9:-1].split(", ")))
    commands = list(map(int, i[1].split(" ")))
    after = list(map(int, i[2][9:-1].split(", ")))
    pInst.append((before, commands, after))

def deepCopy(oldList):
    return [i for i in oldList]
    
def addr (A, B, C, inputList):
    outList = deepCopy(inputList)
    outList[C] = inputList[A] + inputList[B]
    return outList

def addi (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = inputList[A] + B
    return outList

def mulr (A, B, C, inputList):
    outList = deepCopy(inputList)
    outList[C] = inputList[A] * inputList[B]
    return outList

def muli (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = inputList[A] * B
    return outList

def banr (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = (inputList[A] & inputList[B])
    return outList
    
def bani (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = (inputList[A] & B)
    return outList

def borr (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = (inputList[A] | inputList[B])
    return outList

def bori (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = (inputList[A] | B)
    return outList

def setr (A,_,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = inputList[A]
    return outList

def seti (A, _, C, inputList):
    outList = deepCopy(inputList)
    outList[C] = A
    return outList

def gtir (A, B, C, inputList):
    outList = deepCopy(inputList)
    outList[C] = 1 if A > inputList[B] else 0
    return outList

def gtri (A, B, C, inputList):
    outList = deepCopy(inputList)
    outList[C] = 1 if inputList[A] > B else 0
    return outList
    
def gtrr (A, B, C, inputList):
    outList = deepCopy(inputList)
    outList[C] = 1 if inputList[A] > inputList[B] else 0
    return outList
    
def eqir (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = 1 if A == inputList[B] else 0
    return outList

def eqri (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = 1 if inputList[A] == B else 0
    return outList

def eqrr (A,B,C, inputList):
    outList = deepCopy(inputList)
    outList[C] = 1 if inputList[A] == inputList[B] else 0
    return outList
    
procs = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
possibleProcs = [[] for i in range(len(procs))]
part1 = 0
for sId, pi in enumerate(pInst):
    before = pi[0]
    vals = pi[1]
    after = pi[2]
    nMatches = 0
    opCode = vals[0]
    posProcs = []
    for idx, proc in enumerate(procs):
        testAfter = proc(vals[1], vals[2], vals[3] , before)
        if(testAfter == after):
            nMatches += 1
            posProcs.append(idx)
    if(nMatches >= 3):
        part1 += 1
    possibleProcs[opCode].append(posProcs)
print(part1)

opToProcWork = []
opToProc = {}
procToCode = {}
for lists in possibleProcs:
    possibles = set(range(len(procs)))
    for l in lists:
        possibles = possibles.intersection(set(l))
    possibleList = list(possibles)
    opToProcWork.append(possibleList)
    
while(len(opToProc) < len(procs)):
    for opCode, possibleProcs in enumerate(opToProcWork):
        if(len(possibleProcs) == 1):
            opToProc[opCode] = possibleProcs[0]
            procToCode[possibleProcs[0]] = opCode
    for opCode, possibleProcs in enumerate(opToProcWork):
        newList = []
        for possibleProc in possibleProcs:
            if possibleProc not in procToCode:
                newList.append(possibleProc)
        opToProcWork[opCode] = newList

secondpart = secondpart.split("\n")
secondpart = list(map(lambda x: list(map(int, x.split(" "))), secondpart))
regs = [0 for i in range(4)]
for [opcode, A, B, C] in secondpart:
    regs = procs[opToProc[opcode]](A, B, C, regs)
print(regs[0])