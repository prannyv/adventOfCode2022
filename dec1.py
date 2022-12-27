file = open("dec1input.txt", "r")

maxCals = [1,2,3]
curCals = 0
for line in file:
    if len(line.strip()) == 0:
        if curCals > min(maxCals):
            maxCals[maxCals.index(min(maxCals))] = curCals
        curCals = 0
    else:
        curCals += int(line.strip())

print(maxCals[0]+maxCals[1]+maxCals[2])