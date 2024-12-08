def checkR(x, y, letterArray):
    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y][x+1] != 'M':
            return False

        if letterArray[y][x+2] != 'A':
                return False

        if letterArray[y][x+3] != 'S':
                return False
    except:
        return False

    return True

def checkL(x, y, letterArray):
    if (x - 3) < 0:
         return False

    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y][x-1] != 'M':
            return False

        if letterArray[y][x-2] != 'A':
                return False

        if letterArray[y][x-3] != 'S':
                return False
    except:
         return False
    
    return True

def checkU(x, y, letterArray):
    if (y - 3) < 0:
         return False

    try:
        if letterArray[y][x] != 'X':
            return False

        if letterArray[y-1][x] != 'M':
            return False

        if letterArray[y-2][x] != 'A':
                return False

        if letterArray[y-3][x] != 'S':
                return False
    except:
         return False
    
    return True

def checkD(x, y, letterArray):
    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y+1][x] != 'M':
            return False

        if letterArray[y+2][x] != 'A':
                return False

        if letterArray[y+3][x] != 'S':
                return False
    except:
        return False
    
    return True

def checkUL(x, y, letterArray):
    if (x - 3) < 0:
         return False

    if (y - 3) < 0:
         return False

    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y-1][x-1] != 'M':
            return False

        if letterArray[y-2][x-2] != 'A':
                return False

        if letterArray[y-3][x-3] != 'S':
                return False
    except:
        return False
    
    return True

def checkUR(x, y, letterArray):
    if (y - 3) < 0:
         return False

    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y-1][x+1] != 'M':
            return False

        if letterArray[y-2][x+2] != 'A':
                return False

        if letterArray[y-3][x+3] != 'S':
                return False
    except:
        return False
    
    return True

def checkDL(x, y, letterArray):
    if (x - 3) < 0:
         return False

    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y+1][x-1] != 'M':
            return False

        if letterArray[y+2][x-2] != 'A':
                return False

        if letterArray[y+3][x-3] != 'S':
                return False
    except:
        return False
    
    return True

def checkDR(x, y, letterArray):
    try:
        if letterArray[y][x] != 'X':
            return False
        
        if letterArray[y+1][x+1] != 'M':
            return False

        if letterArray[y+2][x+2] != 'A':
                return False

        if letterArray[y+3][x+3] != 'S':
                return False
    except:
        return False
    
    return True

inputFile = open("input.txt", "r")

letterArray = []

for line in inputFile.readlines():
    letterArray.append(list(line.strip()))

inputFile.close()

foundCount = 0

for y in range(len(letterArray)):
    for x in range(len(letterArray[y])):
        if checkR(x, y, letterArray):
            print("Found XMAS at (R): " + str(x) + ", " + str(y))
            foundCount += 1
        
        if checkL(x, y, letterArray):
            print("Found XMAS at (L): " + str(x) + ", " + str(y))
            foundCount += 1
        
        if checkU(x, y, letterArray):
            print("Found XMAS at (U): " + str(x) + ", " + str(y))
            foundCount += 1
        
        if checkD(x, y, letterArray):
            print("Found XMAS at (D): " + str(x) + ", " + str(y))
            foundCount += 1

        if checkUL(x, y, letterArray):
            print("Found XMAS at (UL): " + str(x) + ", " + str(y))
            foundCount += 1

        if checkUR(x, y, letterArray):
            print("Found XMAS at (UR): " + str(x) + ", " + str(y))
            foundCount += 1
        
        if checkDL(x, y, letterArray):
            print("Found XMAS at (DL): " + str(x) + ", " + str(y))
            foundCount += 1

        if checkDR(x, y, letterArray):
            print("Found XMAS at (DR): " + str(x) + ", " + str(y))
            foundCount += 1


print("Total Found: " + str(foundCount))
