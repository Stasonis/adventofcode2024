import copy

class CycleException(Exception):
    pass

def findGuard(map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == '^' or map[row][col] == '>' or map[row][col] == 'V' or map[row][col] == '<':
                return [row, col]
    
    raise Exception

def moveGuard(map, guardPos):
    row = guardPos[0]
    col = guardPos[1]

    match map[row][col]:
        case '^':
            if row == 0:
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row - 1][col] == '#':
                #print("Turning")
                map[row][col] = '>'
                return [row, col]
            else:
                #print("Moving")
                map[row - 1][col] = '^'
                map[row][col] = 'X'
                return [row - 1, col]

            #return True
        case '>':
            if (col + 1) == len(map[row]):
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row][col + 1] == '#':
                #print("Turning")
                map[row][col] = 'V'
                return [row, col]
            else:
                #print("Moving")
                map[row][col+1] = '>'
                map[row][col] = 'X'
                return [row, col + 1]

            #return True
        case 'V':
            if (row + 1) == len(map):
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row + 1][col] == '#':
                #print("Turning")
                map[row][col] = '<'
                return [row, col]
            else:
                #print("Moving")
                map[row + 1][col] = 'V'
                map[row][col] = 'X'
                return [row + 1, col]

            #return True

        case '<':
            if col == 0:
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row][col - 1] == '#':
                #print("Turning")
                map[row][col] = '^'
                return [row, col]
            else:
                #print("Moving")
                map[row][col - 1] = '<'
                map[row][col] = 'X'
                return [row, col - 1]

            #return True
        
    return False

def printMap(map):
    for row in map:
        print(''.join(row))


inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

map = []

for line in lines:
    map.append(list(line.strip()))

i = 0

guardPos = findGuard(map)
guardRow = guardPos[0]
guardCol = guardPos[1]

cycleCount = 0

moveCount = 0
solvedMap = copy.deepcopy(map)

guardPos = findGuard(solvedMap)

while guardPos != False:
    guardPos = moveGuard(solvedMap, guardPos)
    moveCount += 1

print("Solved in " + str(moveCount) + " moves")
printMap(solvedMap)

for row in range(len(map)):

    for col in range(len(map[row])):

        if solvedMap[row][col] != 'X':
            print("Skipping - Not on Path [" + str(row) + "," + str(col) + "]")
            continue

        print("Checking [" + str(row) + "," + str(col) + "]")

        if row == guardRow and col == guardCol:
            continue
        
        if map[row][col] == '#':
            continue

        mapCopy = copy.deepcopy(map)
        moveList = []

        mapCopy[row][col] = '#'

        #try:
        #    while(moveGuard(mapCopy)):
        #        continue
        #except CycleException:
        #    print("Cycle Detected")
        #    cycleCount += 1
        moveCount = 0
        maxMoves = len(mapCopy) * len(mapCopy[0])

        guardPos = findGuard(mapCopy)

        #while (guardPos = moveGuard(mapCopy, guardPos)) != False:
        while guardPos != False:
            guardPos = moveGuard(mapCopy, guardPos)
            moveCount += 1
            if moveCount > maxMoves:
                print("Cycle Found")
                cycleCount += 1
                break
            
print("Cycle Count: " + str(cycleCount))

