with open("input.txt", "r") as infile:
    rails = list(map( list, infile.read().split("\n")))
width = len(rails[0])
height = len(rails)
carts = []
for rowNo, row in enumerate(rails):
    for colNo, cell in enumerate(row):
        if(cell in '^>v<'):
            carts.append({'loc': (colNo, rowNo), 'facing': cell, 'running': True, 'intersection': 0})
        if(cell in '^v'):
            rails[rowNo][colNo] = '|'
        if(cell in '<>'):
            rails[rowNo][colNo] = '-'
t = 0
dirs = '<^>v'
ints = [-1, 0, 1]
nCarts = len(carts)
def cartOrder():
    order = []
    for cartNo, cart in enumerate(carts):
        if(cart['running']):
            order.append((cart['loc'], cartNo))
    return list(map(lambda x: x[1], sorted(order)))
firstCrash = True
while(nCarts > 1):
    t += 1
    if(t>=20000):
        break
    tCO = cartOrder()
    for cartNo in cartOrder():
        cart = carts[cartNo]
        (x,y) = cart['loc']
        f = cart['facing']
        i = cart['intersection']
        if(not cart['running']):
            continue
        if(f == '^'):
            y -= 1
            newLoc = rails[y][x]
            if(newLoc == '\\'):
                f = '<'
            elif(newLoc == '/'):
                f = '>'
            elif(newLoc == '+'):
                f = dirs[(1+ints[i])%4]
                #print('Cart {}: ^ becomes {}'.format(cartNo, f))
                i = (i+1)%3
        elif (f == '>'):
            x += 1
            newLoc = rails[y][x]
            if(newLoc == '\\'):
                f = 'v'
            elif(newLoc == '/'):
                f = '^'
            elif(newLoc == '+'):
                f = dirs[(2+ints[i])%4]
                #print('Cart {}: > becomes {}'.format(cartNo, f))
                i = (i+1)%3
        elif (f == '<'):
            x -=1
            newLoc = rails[y][x]
            if(newLoc == '\\'):
                f = '^'
            elif(newLoc == '/'):
                f = 'v'
            elif(newLoc == '+'):
                f = dirs[(0+ints[i])%4]
                #print('Cart {}: < becomes {}'.format(cartNo, f))
                i = (i+1)%3
        elif (f == 'v'):
            y += 1
            newLoc = rails[y][x]
            if(newLoc == '\\'):
                f = '>'
            elif(newLoc == '/'):
                f = '<'
            elif(newLoc == '+'):
                f = dirs[(3+ints[i])%4]
                #print('Cart {}: v becomes {}'.format(cartNo, f))
                i = (i+1)%3
        
        crashed = False
        for otherCartNo, otherCart in enumerate(carts):
            if(cartNo != otherCartNo and otherCart['loc'] == cart['loc'] and otherCart['running']):
                #print(cart['loc'])
                cart['running'] = False
                otherCart['running'] = False
                nCarts -= 2
                crashed = True
                if(firstCrash):
                    firstCrash = False
                    print("{},{}".format(cart['loc'][0], cart['loc'][1]))
                break
        if(not crashed):
            carts[cartNo] = {'loc': (x,y), 'facing': f, 'intersection': i, 'running': True}
            
for cart in carts:
    if(cart['running']):
        print("{},{}".format(cart['loc'][0], cart['loc'][1]))
