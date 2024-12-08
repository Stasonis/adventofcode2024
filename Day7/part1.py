import copy

inputFile = open("input.txt", "r")
lines = inputFile.readlines()
inputFile.close()

#input = []
operatorArrays = {1: [['+'],['*']]}

def getOperatorArray(numOperators):
    
    if operatorArrays.get(numOperators) == None:
        operators = []

        for item in getOperatorArray(numOperators - 1):
            list1 = copy.deepcopy(item)
            list1.append('+')
            operators.append(list1)

            list2 = copy.deepcopy(item)
            list2.append('*')
            operators.append(list2)
            

        operatorArrays[numOperators] = operators

    return operatorArrays.get(numOperators)

def isValidInputOperator(value, inputs):

    operators = getOperatorArray(len(inputs) - 1)

    for operator in operators:
        if runOperators(operator, inputs) == value:
            return True

    return False

def runOperators(operators, values):
    output = values[0]

    for i in range(len(operators)):
        match operators[i]:
            case '+':
                output += values[i + 1]
            case '*':
                output *= values[i + 1]
    
    return output

validSum = 0;

for line in lines:
    parts = line.split(":")

    parts[0] = int(parts[0])

    parts[1] = parts[1].strip().split()
    parts[1] = [int(item) for item in parts[1]]
    #input.append(parts)
    if isValidInputOperator(parts[0], parts[1]):
        validSum += parts[0]


print("Valid Sum: " + str(validSum))