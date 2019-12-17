with open("input.txt", "r") as infile:
    text = infile.read()

def reduce(text):
    reduced = False

    while(not reduced):
        reduced = True
        index = 0
        while(index < (len(text)-1) ):
            if(text[index].lower() == text[index+1].lower() and text[index] != text[index+1]):
                reduced = False
                leftidx = index
                rightidx = index+1
                while(leftidx != -1 and rightidx != len(text) and text[leftidx].lower() == text[rightidx].lower() and text[leftidx] != text[rightidx]):
                    leftidx -= 1
                    rightidx += 1
                leftidx += 1
                rightidx -= 1
                text = text[:leftidx]+text[rightidx+1:]
            else:
                index += 1
    return (text, len(text))

(reduced, part1) = reduce(text)

print(part1)

#with open("out.txt", "w") as outfile:
#    outfile.write(reduced)
minLen = part1
for i in range(26):
    char = chr(ord('A') + i)
    newtext = ""
    for j in reduced:
        if (j!=char and j!=char.lower()):
            newtext += j
    newLen = reduce(newtext)[1]
    minLen = min(newLen, minLen)
print(minLen)