def sumPartNums(theInputFile):
    total = 0
    lineNum = 0
    inputFile = theInputFile.readlines()
    for line in inputFile:
        #listOfNums has [[num, start pos on line, end pos on line], [...]]
        listOfNums = extractNumbers(line)
        print(listOfNums)

        for number in listOfNums:
            isPartNum = checkIfIsPartNum(number, lineNum, inputFile)

            if isPartNum:
                total = total + number[0]

        lineNum = lineNum + 1

    return total

def extractNumbers(line):
    numList = []
    
    currentNum = ""
    startPosOfNum = 0
    endPosOfNum = 0
    isNumStarted = False
    pos = 0
    for character in line:
        if character.isdigit():
            if not isNumStarted:
                isNumStarted = True
                startPosOfNum = pos
                #print("start pos: " + str(startPosOfNum))
            currentNum = currentNum + character
        else:
            if isNumStarted:
                isNumStarted = False
                endPosOfNum = pos - 1
                #print("end pos: " + str(endPosOfNum))
                numberInfo = [int(currentNum), startPosOfNum, endPosOfNum]
                numList.append(numberInfo)
                currentNum = ""

        pos = pos + 1

    return numList

def checkIfIsPartNum(number, lineNum, inputFile):
    isPartNum = False
    startPos = number[1]
    endPos = number[2]
    #check Line Before
    if((lineNum - 1) >= 0):
        isPartNum = checkLine(startPos, endPos, inputFile[lineNum - 1])
        if isPartNum:
            return True
    #check Line After
    if((lineNum + 1) < len(inputFile)):
        isPartNum = checkLine(startPos, endPos, inputFile[lineNum + 1])
        if isPartNum:
            return True
    #check line of num
    return checkLine(startPos, endPos, inputFile[lineNum])
        
def checkLine(startOfNum, endOfNum, line): 
    startPos = startOfNum
    endPos = endOfNum
    #Added minus 2 since I forgot about newline characters, there is a better way to do this
    if len(line)-2 != endPos:
        endPos = endPos + 1
    if startPos != 0:
        startPos = startPos - 1

    for position in range(startPos, endPos+1):
        character = line[position]
        if not character.isdigit():
            if character != '.':
                return True
    return False
            
            
f = open("input.txt", "r")
print(sumPartNums(f))

