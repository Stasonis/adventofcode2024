inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

def navigateTrailhead(map, row, col):
    peaksFound = {}
    navigateTrailheadHelper(map, row, col, peaksFound)

    peakCount = 0

    for key in peaksFound:
        peakCount += len(peaksFound[key])

    return peakCount


def navigateTrailheadHelper(map, row, col, peaksFound):

    currentVal = map[row][col]

    if currentVal == 9:
        #Found a valid trail
        if(peaksFound.get(row) == None):
            peaksFound[row] = []
        
        try:
            peaksFound[row].index(col)
        except:
            peaksFound[row].append(col)

    searchVal = currentVal + 1

    #Move Left
    if col > 0 and map[row][col - 1] == searchVal:
        navigateTrailheadHelper(map, row, col - 1, peaksFound)
    
    #Move Right
    if (col + 1) < len(map[row]) and map[row][col+1] == searchVal:
        navigateTrailheadHelper(map, row, col + 1, peaksFound)

    #Move Up
    if row > 0 and map[row - 1][col] == searchVal:
        navigateTrailheadHelper(map, row - 1, col, peaksFound)

    #Move down
    if(row + 1) < len(map) and map[row + 1][col] == searchVal:
        navigateTrailheadHelper(map, row + 1, col, peaksFound)

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