def sort(inputFile):
    bigNumList = []
    for line in inputFile:
        numList = []
        for letter in line:
            if letter.isdigit():
                numList += letter
                
        stringNum = (str(numList[0]) + str(numList[-1])) 
        bigNumList.append(stringNum)

    total = 0
    for value in bigNumList:
        total = total + int(value)

    return total

f = open("input.txt", "r")
print(sort(f))

