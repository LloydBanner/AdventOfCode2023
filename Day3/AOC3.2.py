def sumPartNums(theInputFile):
    total = 0
    lineNum = 0
    inputFile = theInputFile.readlines()
    numsWithCogs = []
    for line in inputFile:
        #listOfNums has [[num, start pos on line, end pos on line], [...]]
        listOfNums = extractNumbers(line)

        for number in listOfNums:
            cogs = getAdjacentCogs(number, lineNum, inputFile)

            if cogs != []:
                numsWithCogs.append([number[0], cogs])

        lineNum = lineNum + 1

    total = multiplyAndAddCogs(numsWithCogs)
      
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

def getAdjacentCogs(number, lineNum, inputFile):
    isPartNum = False
    startPos = number[1]
    endPos = number[2]
    #cogs is [[line num, [cog1, cog2, ...]], [line num, [cog1, cog2, ...]], ...]  
    cogs = []
    #check Line Before
    if((lineNum - 1) >= 0):
        cogs.append([lineNum - 1, checkLine(startPos, endPos, inputFile[lineNum - 1])])
    #check Line After
    if((lineNum + 1) < len(inputFile)):
        cogs.append([lineNum + 1, checkLine(startPos, endPos, inputFile[lineNum + 1])])
    #check line of num
    cogs.append([lineNum, checkLine(startPos, endPos, inputFile[lineNum])])
    return cogs

#Returns list of positions with cogs on that line next to the num        
def checkLine(startOfNum, endOfNum, line): 
    startPos = startOfNum
    endPos = endOfNum
    #Added minus 2 since I forgot about newline characters, there is a better way to do this
    if len(line)-2 != endPos:
        endPos = endPos + 1
    if startPos != 0:
        startPos = startPos - 1

    result = []
    for position in range(startPos, endPos+1):
        character = line[position]
        if not character.isdigit():
            if character == '*':
                result.append(position)
    return result

def multiplyAndAddCogs(numsWithCogs):
    cogDict = {}
    for number in numsWithCogs:
        for line in number[1]:
            for cogPos in line[1]:
                cogString = str(line[0]) + ":" + str(cogPos)
                if cogString in cogDict.keys():
                    cogDict[cogString].append(number[0])
                else:
                    cogDict[cogString] = [number[0]]

    total = 0
    print(cogDict)
    for numbers in cogDict.values():
        if len(numbers) == 2:
            product = 1;
            for number in numbers:
                product = product * number
            total = total + product

    return total
        
            
f = open("input.txt", "r")
print(sumPartNums(f))

