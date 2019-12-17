print("Python 3 takes too long to compute, done in C++ instead (see the .cpp file)")
'''
with open("in", "r") as infile:
    lines = infile.read().split("\n") 


ipReg = int(lines[0].split(" ")[1])
commands = []
for line in lines[1:]:
    pars = line.split(" ")
    vals = map(int,pars[1:])
    commands.append((pars[0], *vals))
    
def printRegs():
    print("{} - A:{} B:{} C:{} D:{} E:{} F:{}".format(regs[ipReg], *regs))
regs = [0 for i in range(6)]
regs[0] = 0

vals = set()
while(regs[ipReg] >= 0 and regs[ipReg]<len(commands)):
    
    (op, A, B, C) = commands[regs[ipReg]]
    if(regs[ipReg] == 28):
        if(regs[3] not in vals):
            vals.add(regs[3])
            printRegs()
        else:
            break
    
    if(op == 'addr'):
        regs[C] = regs[A] + regs[B]
    elif(op == 'addi'):
        regs[C] = regs[A] + B
    elif(op == 'mulr'):
        regs[C] = regs[A] * regs[B]
    elif(op == 'muli'):
        regs[C] = regs[A] * B
    elif(op == 'banr'):
        regs[C] = regs[A] & regs[B]
    elif(op == 'bani'):
        regs[C] = regs[A] & B
    elif(op == 'borr'):
        regs[C] = regs[A] | regs[B]
    elif(op == 'bori'):
        regs[C] = regs[A] | B
    elif(op == 'setr'):
        regs[C] = regs[A]
    elif(op == 'seti'):
        regs[C] = A
    elif(op == 'gtir'):
        regs[C] = 1 if A > regs[B] else 0
    elif(op == 'gtri'):
        regs[C] = 1 if regs[A] > B else 0
    elif(op == 'gtrr'):
        regs[C] = 1 if regs[A] > regs[B] else 0
    elif(op == 'eqir'):
        regs[C] = 1 if A == regs[B] else 0
    elif(op == 'eqri'):
        regs[C] = 1 if regs[A] == B else 0
    elif(op == 'eqrr'):
        regs[C] = 1 if regs[A] == regs[B] else 0
    
    regs[ipReg] += 1
'''