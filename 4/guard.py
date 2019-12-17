import re
def gettime(str):

    times = list(map(int,re.findall('(?<![#!\d])([\d]{4}|[\d]{2})', str)))
    return times[0]*(1E8)+times[1]*1E6+times[2]*1E4+times[3]*1E2+times[4]

with open("input.txt", "r") as infile:
    logs = sorted(infile.read().strip().split("\n"), key=gettime)
maxGuard = 0
asleepTimings = {}
for i in logs:
    guard = re.search('(?<=#)([\d]{1,4})', i)
    if(guard != None):
        guard = guard.group(0)
        if (guard not in asleepTimings):
            asleepTimings[guard] = {}


curGuard = '-1'
prevMin = 0
isAsleep = False
for i in logs:
    guard = re.search('(?<=#)([\d]{1,4})', i)
    if(guard != None):
        curGuard = guard.group(0)
        isAsleep = False
    curMin = int(re.search('(?<=:)([\d]{2})', i).group(0))
    curMonth = re.findall('(?<=-)([\d]{2})', i)[0]
    curDay = re.findall('(?<=-)([\d]{2})', i)[1]
    if(isAsleep):
        if(curMonth+curDay not in asleepTimings[curGuard]):
            asleepTimings[curGuard][curMonth+curDay] = []
        asleepTimings[curGuard][curMonth+curDay].append((prevMin, curMin))
    isAsleep = (re.search('(wakes)|(begins)', i) == None)
    prevMin = curMin

maxAsleepTime = 0
maxAsleepGuard = 0
for guard, dates in asleepTimings.items():
    asleepTime = 0
    for date, timeList in dates.items():
        for (start, end) in timeList:
            asleepTime += (int(end)-int(start))
    if(asleepTime > maxAsleepTime):
        maxAsleepGuard = guard
        maxAsleepTime = asleepTime

def within(a,x,b):
    return a<=x and x<b
hour = [0 for i in range(60)]
maxAsleepGuardTimes = asleepTimings[maxAsleepGuard]
for i in range(60):
    for date, timeList in maxAsleepGuardTimes.items():
        for(start, end) in timeList:
            if(within(start, i, end)):
                hour[i]+=1
maxMin = 0
maxCount = 0
for min,count in enumerate(hour):
    if(count > maxCount):
        maxCount = count
        maxMin = min
part1 = maxMin * int(maxAsleepGuard)

hours = [{} for i in range(60)]
for min in range(60):
    for guard, dates in asleepTimings.items():
        for date, timeList in dates.items():
            for (start, end) in timeList:
                if(within(start, min, end)):
                    if(guard not in hours[min]):
                        hours[min][guard] = 0
                    hours[min][guard] += 1
maxMin = 0
maxCount = 0
maxGuard = 0
for min, guards in enumerate(hours):
    for guard, count in guards.items():
        if(count > maxCount):
            maxCount = count
            maxGuard = guard
            maxMin = min
part2 = maxMin * int(maxGuard)
print(part1, part2)
#with open("output.txt", "w") as outfile:
    #outfile.write("\n".join(logs))