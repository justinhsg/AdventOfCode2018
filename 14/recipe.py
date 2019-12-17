with open("input.txt") as infile:
    recipe = int(infile.read())

scores = [3, 7]
e1, e2 = 0, 1
while(len(scores) <= 10+recipe):
    total = scores[e1]+scores[e2]
    scores.extend(divmod(total, 10) if total >= 10 else (total,))
    e1 = (1+e1+scores[e1])%len(scores)
    e2 = (1+e2+scores[e2])%len(scores)
print(''.join(list(map(str, scores[recipe:recipe+10]))))

scores = [3,7]
e1, e2 = 0,1
recAsList = list(map(int, list(str(recipe))))
while(scores[-6:] != recAsList and scores[-7:-1] != recAsList):
    total = scores[e1]+scores[e2]
    scores.extend(divmod(total, 10) if total >= 10 else (total,))
    e1 = (1+e1+scores[e1])%len(scores)
    e2 = (1+e2+scores[e2])%len(scores)
if(scores[-6:] == recAsList):
    print(len(scores)-6)
else:
    print(len(scores)-7)