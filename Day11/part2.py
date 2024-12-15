from functools import lru_cache

inputFile = open("input.txt", "r")
line = inputFile.readline()
inputFile.close()

stones = line.strip().split()

@lru_cache(maxsize=None)
def getStoneSplits(value, blinks):
    if blinks == 0:
        return 0

    if value == '0':
        #stones[index] = '1'
        return getStoneSplits('1', blinks - 1)
    
    if len(value) % 2 == 0:
        #print("Splitting " + value)
        #shiftStones(index)
        midpoint = len(value) // 2

        splits = 1
        splits += getStoneSplits(str(int(value[:midpoint])), blinks - 1)
        splits += getStoneSplits(str(int(value[midpoint:])), blinks - 1)
    
        return splits
    
    else:
        #stones[index] = str(int(value) * 2024)
        return getStoneSplits(str(int(value) * 2024), blinks - 1)

stoneCount = len(stones)

for stone in stones:
    print("Processing Stone " + str(stone))
    stoneCount += getStoneSplits(stone, 75)

print("Total Stones: " + str(stoneCount))