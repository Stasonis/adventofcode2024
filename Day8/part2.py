ants = {}
results = []
grid = []

def addAntinode(row, col):
    print("Adding antinode at [" + str(row) + ", " + str(col) + "]")
    
    if row < 0 or col < 0:
        return False
    if row >= len(grid):
        return False
    
    if col >= len(grid[0]):
        return False
    
    results[row][col] = 'X'

    return True

def findAndAddAntinodes(row1, col1, row2, col2):
    print("[" + str(row1) + ", " + str(col1) + "] - [" + str(row2) + ", " + str(col2) + "]")

    rowDiff = row1 - row2
    colDiff = col1 - col2

    addAntinode(row1, col1)
    addAntinode(row2, col2)

    m = 1
    while addAntinode(row1 + (rowDiff * m), col1 + (colDiff * m)):
        m += 1
    
    m = 1
    while addAntinode(row2 - (rowDiff * m), col2 - (colDiff * m)):
        m += 1



inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()



#Build input structures
for line in lines:
    grid.append(list(line.strip()))

for row in range(len(grid)):

    newRow = []

    for col in range(len(grid[row])):

        newRow.append('.')

        currentChar = grid[row][col]
        if currentChar != '.':

            if ants.get(currentChar) == None:
                ants[currentChar] = []
            
            ants[currentChar].append([row, col])

    results.append(newRow)

#Process inputs    
for key in ants:
    print("Processing " + key)

    antPos = ants.get(key)

    for index1 in range(len(antPos)):
        print("[" + str(antPos[index1][0]) + ", " + str(antPos[index1][1]) + "]")

        for index2 in range(index1 + 1, len(antPos)):
            findAndAddAntinodes(antPos[index1][0], antPos[index1][1], antPos[index2][0], antPos[index2][1])


antiNodeCount = 0
for line in results:

    antiNodeCount += len([i for i, x in enumerate(line) if x == 'X'])

    print(''.join(line))


print("Antinode Count: " + str(antiNodeCount))