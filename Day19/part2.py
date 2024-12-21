import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def canMakeDesign(design):
    global towels

    possibleLayouts = 0

    if len(design) == 0:
        return 1

    for towel in towels:
        if towel == design[0:len(towel)]:
            #print("Towel " + towel + " matches design " + design)
            #if canMakeDesign(design[len(towel):]) != 0:
            #    possibleLayouts += 1
            possibleLayouts += canMakeDesign(design[len(towel):])
    
    return possibleLayouts

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

towels = []
designs = []

for towel in lines[0].split(","):
    towels.append(towel.strip())

#print(towels)
possibleSolutions = 0

for i in range(2, len(lines)):
    print(i)
    possibleSolutions += canMakeDesign(lines[i].strip())
    #if possibleSolutions != 0:
    #    print("Can make " + lines[i].strip() + " " + str(possibleSolutions) + " ways")
        #designs.append(lines[i].strip())

print("Possible Solutions: " + str(possibleSolutions))
#print(designs)
#print("Workable designs: " + str(len(designs)))