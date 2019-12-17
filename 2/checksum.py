with open("input.txt", "r") as infile:
    lines = infile.read().split("\n")
    
nDoub = 0
nTrip = 0
for i in lines:
    for char in i:
        if(i.count(char) == 2):
            nDoub += 1
            break
    for char in i:
        if(i.count(char) == 3):
            nTrip += 1
            break
print(nDoub*nTrip)


minDiff = len(lines[0])
pair = ["", ""];
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        nDiff = 0
        word1 = lines[i]
        word2 = lines[j]
        for k in range(len(word1)):
            if(word1[k] != word2[k]):
                nDiff += 1
                if(nDiff > minDiff):
                    break
        if(nDiff < minDiff):
            pair = [word1, word2]
            minDiff = nDiff
part2 = ''
for i in range(len(pair[0])):
    if(pair[0][i] == pair[1][i]):
        part2+= pair[0][i]
print(part2)
            
        