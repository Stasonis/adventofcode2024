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
    
#leftList.sort()
#rightList.sort()
totalScore = 0

for x in range(len(leftList)):
    multiplier = 0

    for y in range(len(rightList)):
        if leftList[x] == rightList[y]:
            multiplier += 1
    print("Value: " + str(leftList[x]))
    print("Multiplier: " + str(multiplier))

    totalScore += leftList[x] * multiplier
    

print("Total Score: " + str(totalScore))