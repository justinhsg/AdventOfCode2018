with open("input.txt", "r") as infile:
    logs = infile.read().split("\n") 
    
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
    
procs = {'addr': addr, 
        'addi': addi,
        'mulr': mulr,
        'muli': muli,
        'banr': banr,
        'bani': bani,
        'borr': borr,
        'bori': bori,
        'setr': setr,
        'seti': seti,
        'gtri': gtri,
        'gtir': gtir,
        'gtrr': gtrr,
        'eqri': eqri,
        'eqir': eqir,
        'eqrr': eqrr}
    
ip = int(logs[0].split(" ")[1])
commands= []
for i in logs[1:]:
    command = i.split(" ")
    commands.append((command[0], int(command[1]), int(command[2]), int(command[3])))
    
optext = ""
for (idx, command) in enumerate(commands):
    optext += "{}: {}\n".format(idx, command)
    
regs = [0 for i in range(6)] 
regs[0] = 0
ptr = 0
bypass = False
while(ptr >= 0 and ptr < len(commands)):
    regs[ip] = ptr
    command = commands[ptr]
    regs = procs[command[0]](command[1], command[2], command[3], regs)
    ptr = regs[ip]
    ptr += 1
print(regs[0])

#Part 2 requires the sum of factor of 10551305, by inspection of the code

