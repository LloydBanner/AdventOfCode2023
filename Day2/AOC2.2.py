def sort(inputFile):
    productTotal = 0
    for game in inputFile:
        
        idAndContents = game.split(": ")

        listOfResults = idAndContents[1].replace(";", ",").split(", ")

        maxRedSeen = 0
        maxGreenSeen = 0
        maxBlueSeen = 0
        for draw in listOfResults:
            numToColour = draw.split(" ")
            num = int(numToColour[0])
            colour = numToColour[1].strip()
            if colour == "red":
                if num > maxRedSeen:
                    maxRedSeen = num
            elif colour == "green":
                if num > maxGreenSeen:
                    maxGreenSeen = num
            elif colour == "blue":
                if num > maxBlueSeen:
                    maxBlueSeen = num

        product = maxRedSeen * maxGreenSeen * maxBlueSeen                  
        productTotal = productTotal + product

    return productTotal 
        
        




f = open("input2.txt", "r")
print(sort(f))

