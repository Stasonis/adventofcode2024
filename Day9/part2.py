def defragDiskArray(diskArray):    
    endIndex = len(diskArray) - 1
    currentFileIndex = diskArray[endIndex]

    for tailIndex in range(len(diskArray) - 1, -1, -1):
        if currentFileIndex != diskArray[tailIndex]:
            length = endIndex - tailIndex

            if currentFileIndex != '.':
                #print("Found file " + diskArray[endIndex] + " of length " + str(length))

                emptySpaceIndex = findLeftmostEmptySpace(diskArray, length)
                
                if(emptySpaceIndex <= tailIndex):
                    #print("Move " + diskArray[endIndex] + " to " + str(emptySpaceIndex))
                    for i in range(length):
                        diskArray[emptySpaceIndex + i] = currentFileIndex
                        diskArray[tailIndex + i + 1] = '.'
                    
                    #print(''.join(diskArray))



            endIndex = tailIndex
            currentFileIndex = diskArray[endIndex]


def findLeftmostEmptySpace(diskArray, size):
    emptyLen = 0
    for i in range(len(diskArray)):
        if diskArray[i] == '.':
            emptyLen += 1
        else:
            if(emptyLen != 0):
                if emptyLen >= size:
                    return i - emptyLen
                
                emptyLen = 0
    return len(diskArray)

def checkSum(diskArray):
    checkSum = 0
    for i in range(len(diskArray)):
        if diskArray[i] != '.':
            checkSum += i * int(diskArray[i])

    return checkSum

inputFile = open("input.txt", "r")
line = inputFile.readline()
inputFile.close()

diskArray = []
isBlankSpace = False
fileNumber = 0
for char in list(line):

    numIters = int(char)
    if isBlankSpace:
        insertChar = '.'
        isBlankSpace = False
    else:
        insertChar = str(fileNumber)
        fileNumber += 1
        isBlankSpace = True

    for i in range(numIters):
        diskArray.append(insertChar)

print(''.join(diskArray))

defragDiskArray(diskArray)

#while defragDiskArray(diskArray):
#    print(''.join(diskArray))
#    continue

print("Checksum: " + str(checkSum(diskArray)))