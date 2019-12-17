import re
import heapq

with open("in", "r") as infile:
    lines = infile.read().split('\n')

bots = []

strongestBot = (None, None, None, -1e100)
for line in lines:
    splits = re.split(',|<|>, r=', line)
    x,y,z,r = map(int, splits[1:])
    if(r > strongestBot[3]):
        strongestBot = (x,y,z,r)
    bots.append((x,y,z,r))   


    
    
minx = min(map(lambda x:x[0], bots))
maxx = max(map(lambda x:x[0], bots))
miny = min(map(lambda x:x[1], bots))
maxy = max(map(lambda x:x[1], bots))
minz = min(map(lambda x:x[2], bots))
maxz = max(map(lambda x:x[2], bots))

nBotsInRange = 0
for bot in bots:
    botPos = bot[:3]
    distance = 0
    for dim in range(3):
        distance += abs(botPos[dim] - strongestBot[dim])
    if(distance <= strongestBot[3]):
        nBotsInRange += 1
print(nBotsInRange)



def displacement(a):
    return sum(map(abs, a))

class Cube:
    __cubeID = 0
    
    #generate the 8 points of the cube
    #     7-------6
    #    /|      /|
    #   / |     / |
    #  4-------5  |        
    #  |  3----|--2
    #  | /     | /
    #  |/      |/
    #  0-------1
    #
    __genx = (0,1,1,0,0,1,1,0)
    __geny = (0,0,1,1,0,0,1,1)
    __genz = (0,0,0,0,1,1,1,1)
    
    def __init__(self, x, y, z, size):
    
        #Makes sure each cube is unique
        self.__cubeID = Cube.__cubeID
        Cube.__cubeID += 1
        
        #Size of the cube 
        self.__size = size
        self.__width = 2**size
        
        #Holds the 8 points of the cube
        self.__points = ()
        
        #Holds the set of bots if made to find
        self.__bots = None
        
        tmpPoints = []
        
        #The -1 here is so that we get 2**n points per edge (i.e. 0 to 31 instead of 0 to 32)
        for i in range(8):
            tmpPoints.append((x+Cube.__genx[i]*(self.__width-1), 
                              y+Cube.__geny[i]*(self.__width-1), 
                              z+Cube.__genz[i]*(self.__width-1)))
        self.__points = tuple(tmpPoints)

    def getPosition(self):
        if(self.__size == 0):
            return self.__points[0]
        else:
            return None
        
    def findBots(self, givenBots):
        #Finds bots given a list of bots
        
        #Initialises the set
        self.__bots = set()
        
        #Gets the two extremities
        minPoint = self.__points[0]
        maxPoint = self.__points[6]
        
        
        #Iterates through each bot
        for bot in givenBots:
            
            botPos = tuple(bot[:3])
            botr = bot[3]
            
            #if the a dimension of the bot is within the extremities
            #we ignore that coordinate when finding the manhattan distance
            #since for that distance the value is zero
            toCalc = [False, False, False]
            for dim in range(3):
                if(botPos[dim] < minPoint[dim] or botPos[dim] > maxPoint[dim]):
                    toCalc[dim] = True
            
            
            #iterating through all the points
            for point in self.__points:
                dist = 0
                for dim in range(3):
                    if(toCalc[dim]):
                        dist += abs(botPos[dim] - point[dim])
                #Add to set if within range
                if(dist <= botr):
                    self.__bots.add(bot)
                    break
    
    def getValue(self):
        #Creates a tuple for the priority queue to ordered by set size (decreasing), cube size (increasing), then distance from origin (increasing)
        return (-len(self.__bots), 
                self.__size, 
                displacement(self.__points[0]), 
                self.__cubeID)
    
    def isUnit(self):
        #If cube has size zero, it is just a point
        return self.__size == 0
    
    def subdivide(self):
        #Splits the cube into 8 smaller cubes, can only do so if:
        #The cube has size > 0 and if the cube has a set initialised
        if(self.__size == 0 or self.__bots == None):
            return None
        else:
            newCubes = []
            (x,y,z) = self.__points[0]
            
            #Generates the 8 new start points of the cube (similar to finding the 8 points)
            #from 0-63 (width=64), we want cubes 0-31 and 32-63
            #Then finds bots in range, given the set from the parent cube
            #(Bots out of range of parent are guaranteed to be out of range of child)
            for i in range(8):
                tCube = Cube(x+Cube.__genx[i]*(self.__width//2),
                             y+Cube.__geny[i]*(self.__width//2),
                             z+Cube.__genz[i]*(self.__width//2),
                             self.__size-1)
                tCube.findBots(self.__bots)
                newCubes.append(tCube)
            return newCubes


#Start with a cube that has all bots within (trivially all bots in range)
xRange = maxx - minx
yRange = maxy - miny
zRange = maxz - minz
initSize = 0
initWidth = 1
while(initWidth < xRange or initWidth < yRange or initWidth < zRange):
    initSize += 1
    initWidth = 2**initSize

startCube = Cube(minx, miny, minz, initSize)
startCube.findBots(bots)


toDivide = []
heapq.heappush(toDivide, (startCube.getValue(), startCube))
closestPoint = None

#Continually pop off the cube with the greatest number of bots in range
#If it is a bigger cube, we subdivide the cube and enqueue all the smaller cubes
#The first time we pop off a cube with size 0, we are done.
while(len(toDivide) != 0):
    (val, cube) = heapq.heappop(toDivide)
    if(cube.isUnit()):        
        closestPoint = cube.getPosition()
        break
    else:
        smallCubes = cube.subdivide()
        for cube in smallCubes:
            heapq.heappush(toDivide, (cube.getValue(), cube))
            
print(displacement(closestPoint))
