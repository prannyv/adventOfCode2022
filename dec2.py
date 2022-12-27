file = open("dec2input.txt","r")


totalScore = 0
for line in file:
    line = line.strip()
    curScore = 0

    if line[0] == "A" and line[2] == "X":
        curScore = 3
    elif line[0] == "B" and line[2] == "X":
        curScore = 1
    elif line[0] == "C" and line[2] == "X":
        curScore = 2

    elif line[0] == "A" and line[2] == "Y":
        curScore = 4
    elif line[0] == "B" and line[2] == "Y":
        curScore = 5
    elif line[0] == "C" and line[2] == "Y":
        curScore = 6

    elif line[0] == "A" and line[2] == "Z":
        curScore = 8
    elif line[0] == "B" and line[2] == "Z":
        curScore = 9
    elif line[0] == "C" and line[2] == "Z":
        curScore = 7

    totalScore += curScore

print(totalScore)
