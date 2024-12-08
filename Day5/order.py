import math

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

def checkUpdate(rules, update):
    for rule in rules:
        if checkRule(rule, update) == False:
            print("Rule Failed: " + str(rule) + " " + str(update))
            return False

    return True

def checkRule(rule, update):
    
    try:
        index1 = update.index(rule[0])
        index2 = update.index(rule[1])

        return index1 < index2
    except:
        return True

def getCorrectedUpdate(rules, update):

    for rule in rules:
        if checkRule(rule, update) == False:
            print("Rule Failed: " + str(rule) + " " + str(update))

            correctedUpdate = update.copy()
            #fixIndex = correctedUpdate.index(rule[1])
            #correctedUpdate[fixIndex] = correctedUpdate[fixIndex + 1]
            #correctedUpdate[fixIndex + 1] = rule[1]
            index1 = correctedUpdate.index(rule[0])
            index2 = correctedUpdate.index(rule[1])

            correctedUpdate[index1] = rule[1]
            correctedUpdate[index2] = rule[0]

            return getCorrectedUpdate(rules, correctedUpdate)

    return update
    

rules = []
updates = []

for line in lines:
    if len(line.strip()) > 0:
        if line.find("|") >= 0:
            rule = line.strip().split("|")
            rules.append(rule)
        else:
            updates.append(line.strip().split(","))

goodUpdates = 0
midpointSum = 0
#print(rules)

for update in updates:
    
    updatePass = checkUpdate(rules, update)

    if updatePass:
        #midpoint = math.floor(len(update) / 2)
        #midpointSum += int(update[midpoint])
        #print("Update passed: " + str(update) + "Midpoint: " + update[midpoint])
        goodUpdates += 1
    else:
        print("Update failed: " + str(update))
        correctedUpdate = getCorrectedUpdate(rules, update)
        

        midpoint = math.floor(len(correctedUpdate) / 2)
        midpointSum += int(correctedUpdate[midpoint])

        print("Corrected: " + str(correctedUpdate) + "Midpoint: " + correctedUpdate[midpoint])

        goodUpdates += 0

print("Good Updates: " + str(goodUpdates))
print("Midpoint Sum: " + str(midpointSum))