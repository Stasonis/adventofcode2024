def defragDiskArray(diskArray):

    firstOpenSpace = diskArray.index('.')
    lastFullSpace = 0

    for i in range(len(diskArray)):
        if diskArray[len(diskArray) - i - 1] != '.':
            lastFullSpace =  len(diskArray) - i - 1
            break

    if firstOpenSpace >= lastFullSpace:
        return False

    diskArray[firstOpenSpace] = diskArray[lastFullSpace]
    diskArray[lastFullSpace] = '.'

    return True

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

while defragDiskArray(diskArray):
    #print(''.join(diskArray))
    continue


print("Checksum: " + str(checkSum(diskArray)))