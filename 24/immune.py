import re
with open("in", "r") as infile:
    chunk = infile.read()
    
immunesys, infection = chunk.split("\n\nInfection:\n")
infection = infection.split("\n")
immunesys = immunesys.split("\n")[1:]

def parseLine(line):
    words = line.split(" ")
    troops = dict()
    troops['size'] = int(words[0])
    troops['hp'] = int(words[4])
    troops['damage'] = int(words[-6])
    troops['damageType'] = words[-5]
    troops['initiative'] = int(words[-1])
    troops['immunities'] = []
    troops['weaknesses'] = []
    if '(' in line:
        iws = re.split("\(|\)", line)[1]
        statements = iws.split("; ")
        
        for statement in statements:
            iw, type = statement.split(" to ")
            if(iw == 'immune'):
                troops['immunities'] = type.split(", ")
            else:
                troops['weaknesses'] = type.split(", ")
    return troops
    

#print(immunesys)
#print("\n\n")
#print(infection)
#print(parseLine(immunesys[0]))
troopNames = "ABCDEFGHIJKLMN"
immuneTroops = dict()
immuneLeft = dict()
initiativeOrder = list()

for i in range(len(immunesys)):
    immuneTroops[troopNames[i]] = parseLine(immunesys[i])
    immuneLeft[troopNames[i]] = immuneTroops[troopNames[i]]['size']
    initiativeOrder.append((immuneTroops[troopNames[i]]['initiative'], 'imm', troopNames[i]))

infectTroops = dict()
infectLeft = dict()
for i in range(len(infection)):
    infectTroops[troopNames[i]] = parseLine(infection[i])
    infectLeft[troopNames[i]] = infectTroops[troopNames[i]]['size']
    initiativeOrder.append((infectTroops[troopNames[i]]['initiative'], 'inf', troopNames[i]))
    
initiativeOrder.sort(reverse=True)
def battle(boost):
    immuneLeft = dict()
    
    for t in immuneTroops:
        immuneLeft[t] = immuneTroops[t]['size']
        
    infectLeft = dict()
    
    for t in infectTroops:
        infectLeft[t] = infectTroops[t]['size']
        
    while (len(immuneLeft) != 0 and len(infectLeft) != 0):
        #Troop Selection:
        immEffPow = []
        immLeftDupe = dict()
        for t in immuneLeft:
            immEffPow.append((immuneLeft[t] * (immuneTroops[t]['damage']+boost) * 100 + immuneTroops[t]['initiative'], t))
            immLeftDupe[t] = immuneLeft[t]
        immEffPow.sort(reverse=True)

        
        infEffPow = []
        infLeftDupe = dict()
        for t in infectLeft:
            infEffPow.append((infectLeft[t] * infectTroops[t]['damage'] * 100 + infectTroops[t]['initiative'], t))
            infLeftDupe[t] = infectLeft[t]
        infEffPow.sort(reverse=True)

        #Immune
        
        immTargetMap = dict()
        immTargeted = set()
        infTargetMap = dict()
        infTargeted = set()
        
        
        for _,t in immEffPow:
            target = None
            maxDamage = 0
            damageType = immuneTroops[t]['damageType']
            damage = immuneTroops[t]['damage']
            expDamage = (damage+boost)*immuneLeft[t]
            for _, e in infEffPow:
                if(e not in immTargeted):
                    if(damageType not in infectTroops[e]['immunities']):
                        if(damageType in infectTroops[e]['weaknesses']):
                            totDamage = 2*expDamage
                        else:
                            totDamage = expDamage
                        if(totDamage > maxDamage):
                            maxDamage = totDamage
                            target = e
            if(target != None):
                immTargetMap[t]=target
                immTargeted.add(target)
        
        
        for _,t in infEffPow:
            target = None
            maxDamage = 0
            damageType = infectTroops[t]['damageType']
            damage = infectTroops[t]['damage']
            expDamage = damage*infectLeft[t]
            for _, e in immEffPow:
                if(e not in infTargeted):
                    if(damageType not in immuneTroops[e]['immunities']):
                        if(damageType in immuneTroops[e]['weaknesses']):
                            totDamage = 2*expDamage
                        else:
                            totDamage = expDamage
                        if(totDamage > maxDamage):
                            maxDamage = totDamage
                            target = e
            if(target != None):
                infTargetMap[t]=target
                infTargeted.add(target)
        hasChange = False
        for _, team, t in initiativeOrder:
            if(team == 'imm'):
                if(t in immuneLeft and t in immTargetMap):
                    target = immTargetMap[t]
                    
                    if(target in infectLeft):
                        damage = immuneLeft[t]*(immuneTroops[t]['damage']+boost)
                        
                        if(immuneTroops[t]['damageType'] in infectTroops[target]['weaknesses']):
                            damage *= 2
                        nUnits = damage // infectTroops[target]['hp']
                        infectLeft[target] -= nUnits
                        hasChange = True if nUnits > 0 else hasChange
                        if(infectLeft[target] <= 0):
                            infectLeft.pop(target)
            else:
                if(t in infectLeft and t in infTargetMap):
                    target = infTargetMap[t]
                    if(target in immuneLeft):
                        damage = infectLeft[t]*infectTroops[t]['damage']
                        
                        if(infectTroops[t]['damageType'] in immuneTroops[target]['weaknesses']):
                            damage *= 2
                        nUnits = damage // immuneTroops[target]['hp']
                        immuneLeft[target] -= nUnits
                        hasChange = True if nUnits > 0 else hasChange
                        if(immuneLeft[target] <= 0):
                            immuneLeft.pop(target)
        if(not hasChange):
            return ('draw', 0)
    if(len(immuneLeft) == 0):
        remaining = 0
        for t in infectLeft:
            remaining += infectLeft[t]      
        return ('inf', remaining)
    elif(len(infectLeft) == 0):
        remaining = 0
        for t in immuneLeft:
            remaining += immuneLeft[t]
        return ('imm', remaining)
        
print(battle(0)[1])

lb = 0
ub = 100
finalLeft = 0
while(ub - lb > 1):
    newpt = (lb+ub)//2
    res, finalLeft = battle(newpt)
    print("{} -> {}".format(newpt, res))
    if(res == 'imm'):
        ub = newpt
    elif(res == 'inf' or res =='draw'):
        lb = newpt
print(lb, ub, finalLeft)


    