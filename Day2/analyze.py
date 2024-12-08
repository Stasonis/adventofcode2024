def isSafeReport(report):
    increasing = int(report[0]) < int(report[1])

    for x in range(len(report) - 1):
        diff = int(report[x+1]) - int(report[x])
        

        if abs(diff) > 3:
            return False
        
        if increasing:
            if diff <= 0:
                return False
        else:
            if diff >= 0:
                return False
    
    return True

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

safeReports = 0

for line in lines:
    levels = line.split()
    increasing = int(levels[0]) < int(levels[1])
    safe = isSafeReport(levels)
    
    if safe == False:
        for x in range(len(levels)): 
            levelsCopy = levels.copy()
            del levelsCopy[x]

            safe = isSafeReport(levelsCopy)

            if safe:
                break

    if safe:
        safeReports += 1
        print("SAFE")
    else:
        print("UNSAFE")

print("Safe Reports: " + str(safeReports))

