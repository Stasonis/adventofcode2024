import re

def processMul(input):
    input = input.replace("mul(", "")
    input = input.replace(")", "")
    numbers = input.split(",")
    num1 = int(numbers[0].strip())
    num2 = int(numbers[1].strip())

    #print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
    return num1 * num2
    

inputFile = open("input.txt", "r")
input = inputFile.read()
inputFile.close()

#print(input)

print("Matches: " + str(len(re.findall("don't\(\).*?do\(\)", input))))

strippedInput = re.sub("don't\(\).*?do\(\)", "", input)
#print(strippedInput)

matches = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", strippedInput)

#print(matches)

total = 0

for match in matches:
    total += processMul(match)

print("Total: " + str(total))