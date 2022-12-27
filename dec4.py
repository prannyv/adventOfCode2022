input = open("dec4input.txt", "r")

count = 0

def makeList(nums):
    list = []
    num1 = int(nums[0])
    num2 = int(nums[1])
    for i in range(num1,num2+1):
        list.append(i)
    return list


for line in input:
    curNums = []
    #curNums = [[numlist1], [numlist2]]
    line = line.strip().split(",")
    for pair in line:
        curNums.append(makeList(pair.split("-")))
    for num in curNums[0]:
        if num in curNums[1]:
            count+=1
            break;



    # if int(curNums[0][0]) <= int(curNums[1][0]) and int(curNums[0][1]) >= int(curNums[1][1]):
    #     count += 1
    # elif int(curNums[0][0]) >= int(curNums[1][0]) and int(curNums[0][1]) <= int(curNums[1][1]):
    #     count+=1




print(count)