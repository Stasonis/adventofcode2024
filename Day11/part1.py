inputFile = open("input.txt", "r")
line = inputFile.readline()
inputFile.close()

stones = line.strip().split()

def blink():
    for index in range(len(stones) - 1, -1, -1):
        applyStoneRule(index)

def applyStoneRule(index):
    value = stones[index]

    if value == '0':
        stones[index] = '1'
        return
    
    if len(value) % 2 == 0:
        #print("Splitting " + value)
        shiftStones(index)
        midpoint = len(value) // 2
        stones[index] = str(int(value[:midpoint]))
        stones[index + 1] = str(int(value[midpoint:]))
        return
    
    else:
        stones[index] = str(int(value) * 2024)

def shiftStones(startingIndex):
    endIndex = len(stones)

    #print("Before Shift (" + str(startingIndex) + ", " + str(endIndex) + ")")
    #print(stones)

    stones.append('0')

    swap = len(stones) - 1
    while swap > startingIndex:
        #print("Swapping " + str(i + 1) + " for " + str(i))
        stones[swap] = stones[swap - 1]
        swap -= 1

    #print("After Shift")
    #print(stones)

for i in range(25):
    print("Blink " + str(i))
    blink()
    #print(stones)

print("Total Stones: " + str(len(stones)))