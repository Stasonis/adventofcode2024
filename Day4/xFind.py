def checkRotation1(x, y, letterArray):
    try:        
        if letterArray[y-1][x-1] != 'M':
            return False
        
        if letterArray[y+1][x-1] != 'M':
            return False
        
        if letterArray[y-1][x+1] != 'S':
            return False
        
        if letterArray[y+1][x+1] != 'S':
            return False
    except:
        return False
    
    return True
    
def checkRotation2(x, y, letterArray):
    try:        
        if letterArray[y-1][x-1] != 'S':
            return False
        
        if letterArray[y+1][x-1] != 'M':
            return False
        
        if letterArray[y-1][x+1] != 'S':
            return False
        
        if letterArray[y+1][x+1] != 'M':
            return False
    except:
        return False
    
    return True

def checkRotation3(x, y, letterArray):
    try:        
        if letterArray[y-1][x-1] != 'S':
            return False
        
        if letterArray[y+1][x-1] != 'S':
            return False
        
        if letterArray[y-1][x+1] != 'M':
            return False
        
        if letterArray[y+1][x+1] != 'M':
            return False
    except:
        return False
    
    return True

def checkRotation4(x, y, letterArray):
    try:        
        if letterArray[y-1][x-1] != 'M':
            return False
        
        if letterArray[y+1][x-1] != 'S':
            return False
        
        if letterArray[y-1][x+1] != 'M':
            return False
        
        if letterArray[y+1][x+1] != 'S':
            return False
    except:
        return False
    
    return True

def checkLocation(x, y, letterArray):
    if x == 0:
        return False
    
    if y == 0:
        return False

    try:
        if letterArray[y][x] != 'A':
            return False
        
        if checkRotation1(x, y, letterArray):
            return True
        if checkRotation2(x, y, letterArray):
            return True
        if checkRotation3(x, y, letterArray):
            return True
        if checkRotation4(x, y, letterArray):
            return True

    except:
        return False
    
    return False

inputFile = open("input.txt", "r")

letterArray = []

for line in inputFile.readlines():
    letterArray.append(list(line.strip()))

inputFile.close()

foundCount = 0

for y in range(len(letterArray)):
    for x in range(len(letterArray[y])):
        if checkLocation(x, y, letterArray):
            print("Found One: " + str(x) + "," + str(y))
            foundCount += 1


print("Total Found: " + str(foundCount))
