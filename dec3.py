input = open("dec3input.txt", "r")

def itemCheck(thing1,thing2):
    for item in thing1:
        if item in thing2:
            return item

def itemCheck(thing1,thing2,thing3):
    for item in thing1:
        if item in thing2 and item in thing3:
            return item


count = 0
# for line in input:
#     line = line.strip()
#     sackL = line[:len(line)//2]
#     sackR = line[len(line)//2:]
#     curVal = itemCheck(sackL,sackR)
#     if curVal.islower():
#         count += ord(curVal)-96
#     else:
#         count+= ord(curVal)-38

for line in input:
    line1 = line.strip()
    line2 = input.readline().strip()
    line3 = input.readline().strip()
    curVal = itemCheck(line1,line2,line3)
    if curVal.islower():
        count += ord(curVal)-96
    else:
        count+= ord(curVal)-38
print(count)



