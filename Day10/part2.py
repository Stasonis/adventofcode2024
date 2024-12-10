inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

def navigateTrailhead(map, row, col):

    currentVal = map[row][col]

    trailScore = 0

    if currentVal == 9:
        #Found a valid trail
        return 1

    searchVal = currentVal + 1

    #Move Left
    if col > 0 and map[row][col - 1] == searchVal:
        #print("Moving left")
        trailScore += navigateTrailhead(map, row, col - 1)
    
    #Move Right
    if (col + 1) < len(map[row]) and map[row][col+1] == searchVal:
        #print("Moving right")
        trailScore += navigateTrailhead(map, row, col + 1)

    #Move Up
    if row > 0 and map[row - 1][col] == searchVal:
        #print("Moving Up")
        trailScore += navigateTrailhead(map, row - 1, col)

    #Move down
    if(row + 1) < len(map) and map[row + 1][col] == searchVal:
        #print("Moving down")
        trailScore += navigateTrailhead(map, row + 1, col)
    
    return trailScore

map = []

for line in lines:
    row = list(line.strip())
    map.append([int(item) for item in row])

totalTrailScore = 0

for row in range(len(map)):
    for col in range(len(map[row])):
        if map[row][col] == 0:
            totalTrailScore += navigateTrailhead(map, row, col)
        

print("Total Trail Score: " + str(totalTrailScore))