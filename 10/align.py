import re
with open("input.txt", "r") as infile:
    input = infile.read().rstrip("\n").split("\n")
stars = [[int(i) for i in re.findall(r'-?\d+', line)] for line in input]

mini = 10e10
minw = 10e10
minh = 10e10
for i in range(30000):
    minx = min(i*star[2]+star[0] for star in stars)
    miny = min(i*star[3]+star[1] for star in stars)
    maxx = max(i*star[2]+star[0] for star in stars)
    maxy = max(i*star[3]+star[1] for star in stars)
    if((maxx - minx) < minw) and ((maxy-miny) < minh):
        #print(i, maxx-minx, maxy-miny)
        mini = i
        minw = maxx - minx
        minh = maxy - miny
    if(i - mini >= 50):
        break



for i in range(mini-2, mini+2):
    minx = min(i*star[2]+star[0] for star in stars)
    miny = min(i*star[3]+star[1] for star in stars)
    maxx = max(i*star[2]+star[0] for star in stars)
    maxy = max(i*star[3]+star[1] for star in stars)
    w = maxx - minx
    h = maxy -miny
    #print(minx, miny, maxx, maxy, w, h)
    canvas = [['.' for i in range(w+1)] for i in range(h+1)]
    for star in stars:
        col = i*star[2]+star[0]-minx
        row = i*star[3]+star[1]-miny
        #print(col, row)
        canvas[row][col] = '#'
    print("{}:".format(i))
    print('\n'.join(list(map(lambda x: ''.join(x), canvas))))