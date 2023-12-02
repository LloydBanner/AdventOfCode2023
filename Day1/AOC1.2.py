#This does not feel like a great way to do this but I didn't have much time for this one

stringDigits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def sort(inputFile):
    bigNumList = []
    for line in inputFile:
        numList = []

        positions = []
        intNum = 1
        for num in stringDigits:
            testLine = line
            lengthRemoved = 0;
            while num in testLine:
                numPos = testLine.find(num)
                testLine = testLine[numPos+len(num):]
                positions.append([intNum, numPos+lengthRemoved])
                lengthRemoved += numPos+len(num)
            intNum += 1

        linePos = 0
        for letter in line:
            if letter.isdigit():
                positions.append([letter, linePos])
            linePos += 1

        print(positions)

        greatestPositonNum = [0, -1]
        smallestPositionNum = [0, 10000000000]
        for numToPos in positions:
            print(numToPos)
            if numToPos[1] < smallestPositionNum[1]:
                smallestPositionNum = numToPos
            if numToPos[1] > greatestPositonNum[1]:
                greatestPositonNum = numToPos    

        print("here sum = " + str(smallestPositionNum[0]) + str(greatestPositonNum[0]))
        stringNum = (str(smallestPositionNum[0]) + str(greatestPositonNum[0])) 
        bigNumList.append(stringNum)

    total = 0
    for value in bigNumList:
        total = total + int(value)
        print(total)

    return total

f = open("input.txt", "r")
print(sort(f))

