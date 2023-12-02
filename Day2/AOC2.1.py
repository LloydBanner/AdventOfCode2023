def sort(inputFile):
    numRed = 12
    numGreen = 13
    numBlue = 14

    gameNumTotal = 0;
    for game in inputFile:
        possible = True;
        
        idAndContents = game.split(": ")
        gameName = idAndContents[0]
        idNum = int(gameName.split("Game ")[1])

        listOfResults = idAndContents[1].replace(";", ",").split(", ")
        for draw in listOfResults:
            numToColour = draw.split(" ")
            num = int(numToColour[0])
            colour = numToColour[1].strip()
            if colour == "red":
                if num > numRed:
                    possible = False
                    break
            elif colour == "green":
                if num > numGreen:
                    possible = False
                    break
            elif colour == "blue":
                if num > numBlue:
                    possible = False
                    break

        if possible:
            gameNumTotal = gameNumTotal + idNum

    return gameNumTotal 
        
        




f = open("input2.txt", "r")
print(sort(f))

