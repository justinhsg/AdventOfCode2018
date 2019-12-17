with open("in.txt", "r") as infile:
    text = infile.read().rstrip("\n")
    
nPlayers = int(text.split()[0])
nMarbles = int(text.split()[6])

class llElement:
    
    def __init__(self, val):
        self.value = val
        self.prevElement = self
        self.nextElement = self
    
    def getValue(self):
        return self.value
        
    def setPrev(self, nPrev):
        self.prevElement = nPrev
    
    def getPrev(self):
        return self.prevElement
    
    def setNext(self, nNext):
        self.nextElement = nNext
    
    def getNext(self):
        return self.nextElement
        
        
def travCW(curElement, n):
    tEl = curElement
    for i in range(n):
        tEl = tEl.getNext()
    return tEl
def travCCW(curElement, n):
    tEl = curElement
    for i in range(n):
        tEl = tEl.getPrev()
    return tEl

def highScore(nPlayers, nMarbles):
    curMarb = llElement(0)
    scores = [0 for i in range(nPlayers)]
    for i in range(1, nMarbles+1):
        if((i*10)%nMarbles == 0):
            print("{}%".format(((i)*100)//nMarbles), end='\r')
        curElf =  i%nPlayers
        if(i%23 != 0):
            leftMarb = travCW(curMarb, 1)
            rightMarb = travCW(curMarb, 2)
            newMarb = llElement(i)
            leftMarb.setNext(newMarb)
            rightMarb.setPrev(newMarb)
            newMarb.setNext(rightMarb)
            newMarb.setPrev(leftMarb)
            curMarb = newMarb
        else:
            scores[curElf] += i
            leftMarb = travCCW(curMarb, 8)
            rightMarb = travCCW(curMarb, 6)
            remMarb = travCCW(curMarb, 7)
            scores[curElf] += remMarb.getValue()
            leftMarb.setNext(rightMarb)
            rightMarb.setPrev(leftMarb)
            curMarb = rightMarb
            del remMarb
    return max(scores)
    

part1 = highScore(nPlayers, nMarbles)
print(" "*8, end='\r')
part2 = highScore(nPlayers, nMarbles*100)
print("Part 1: {}\nPart 2: {}".format(part1, part2))