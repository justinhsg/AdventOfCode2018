from functools import reduce
with open("input.txt", "r") as infile:
    processed = str(infile.read()).split("\n")
    
part1 = reduce(lambda x,y: x+y, map(int, processed))

freqs = set()
acc = 0
part2 = False
part2flag = False
while(not part2flag):
    for i in processed:
        acc += int(i)
        if (acc in freqs):
            part2 = acc
            part2flag = True
            break
        else:
            freqs.add(acc)
print(part1)
print(part2)