import re

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

def tokensToSolve(prize):
    tokens = 0

    top = prize["X"] - ((prize["BX"] / prize["BY"]) * prize["Y"])
    divisor = prize["AX"] - (prize["BX"] / prize["BY"] * prize["AY"])
    aPressRaw = top / divisor
    aPress = round(aPressRaw)

    bPressRaw = (prize["Y"] - (prize["AY"] * aPress)) / prize["BY"]
    bPress = round(bPressRaw)

    print("A-Press: " + str(aPress))
    print("B-Press: " + str(bPress))

    if abs(aPress - aPressRaw) < .00001 and abs(bPress - bPressRaw) < .00001:
        print("VALID")
        return (aPress * 3) + bPress

    

    return 0


totalTokens = 0

for i in range(0, len(lines), 4):
    matches = re.findall(r'Button [A,B]: X\+([0-9]+), Y\+([0-9]+)', lines[i])

    prize = {}

    prize["AX"] = int(matches[0][0])
    prize["AY"] = int(matches[0][1])

    matches = re.findall(r'Button [A,B]: X\+([0-9]+), Y\+([0-9]+)', lines[i + 1])

    prize["BX"] = int(matches[0][0])
    prize["BY"] = int(matches[0][1])

    matches = re.findall("Prize: X=([0-9]+), Y=([0-9]+)", lines[i + 2])

    prize["X"] = int(matches[0][0])
    prize["Y"] = int(matches[0][1])

    totalTokens += tokensToSolve(prize)

print("Total Tokens: " + str(totalTokens))