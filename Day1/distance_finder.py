inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

print(len(lines))

leftList = []
rightList = []

for line in lines:
    temp = line.split()

    leftList.append(int(temp[0]))
    rightList.append(int(temp[1]))
    
leftList.sort()
rightList.sort()
totalDiff = 0

for i in range(len(leftList)):
    diff = abs(leftList[i] - rightList[i])
    totalDiff += diff
    print(str(leftList[i]) + " " + str(rightList[i]) + " = " + str(diff))

print("Total Diff: " + str(totalDiff))