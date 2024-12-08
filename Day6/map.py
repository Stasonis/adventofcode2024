import copy

class CycleException(Exception):
    pass

def findGuard(map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == '^' or map[row][col] == '>' or map[row][col] == 'V' or map[row][col] == '<':
                return [row, col]
    
    raise Exception

def moveGuard(map):

    try:
        guardPos = findGuard(map)
        row = guardPos[0]
        col = guardPos[1]
    except:
        print("Couldn't find guard")
        printMap(map)
        return False

    match map[row][col]:
        case '^':
            if row == 0:
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row - 1][col] == '#':
                #print("Turning")
                map[row][col] = '>'
            else:
                #print("Moving")
                map[row - 1][col] = '^'
                map[row][col] = 'X'

            return True
        case '>':
            if (col + 1) == len(map[row]):
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row][col + 1] == '#':
                #print("Turning")
                map[row][col] = 'V'
            else:
                #print("Moving")
                map[row][col+1] = '>'
                map[row][col] = 'X'

            return True
        case 'V':
            if (row + 1) == len(map):
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row + 1][col] == '#':
                #print("Turning")
                map[row][col] = '<'
            else:
                #print("Moving")
                map[row + 1][col] = 'V'
                map[row][col] = 'X'

            return True

        case '<':
            if col == 0:
                #print("Edge of map")
                map[row][col] = 'X'
                return False
            
            if map[row][col - 1] == '#':
                #print("Turning")
                map[row][col] = '^'
            else:
                #print("Moving")
                map[row][col - 1] = '<'
                map[row][col] = 'X'

            return True
        
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

#for row in range(len(map)):

#    for col in range(len(map[row])):

#        print("Checking [" + str(row) + "," + str(col) + "]")

#        if row == guardRow and col == guardCol:
#            continue
        
#        if map[row][col] == '#':
#            continue

#        mapCopy1 = copy.deepcopy(map)

#        mapCopy1[row][col] = '#'

#        mapCopy2 = copy.deepcopy(mapCopy1)

#        while moveGuard(mapCopy1):
#            moveGuard(mapCopy1)
#            moveGuard(mapCopy2)

#            try:
#                guard1Pos = findGuard(mapCopy1)
#                guard2Pos = findGuard(mapCopy2)
#            except:
#                break

#            if guard1Pos[0] == guard2Pos[0] and guard1Pos[1] == guard2Pos[1] and mapCopy1[guard1Pos[0]][guard1Pos[1]] == mapCopy2[guard1Pos[0]][guard1Pos[1]]:
#                print("Found cycle [" + str(row) + "," + str(col) + "]")
                #printMap(mapCopy1)
#                cycleCount += 1
#                break

moveCount = 0
solvedMap = copy.deepcopy(map)
while moveGuard(solvedMap):
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

        while moveGuard(mapCopy):
            moveCount += 1
            if moveCount > maxMoves:
                print("Cycle Found")
                cycleCount += 1
                break
            #try:
            #    guardPos = findGuard(mapCopy)

            #    moveString = mapCopy[guardPos[0]][guardPos[1]] + str(guardPos[0]) + str(guardPos[1])
            #    try:
            #        moveList.index(moveString)
            #        print("Cycle found")
            #        cycleCount += 1
            #        break
            #    except:
            #        moveList.append(moveString)
            #except:
            #    print("BOOOO")
            #    break
            
print("Cycle Count: " + str(cycleCount))

