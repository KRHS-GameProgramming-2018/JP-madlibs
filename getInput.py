def getMenuInput():
    goodInput = False
    while not goodInput:
        response = raw_input(" > ")
        if (response == "1" 
            or response == "One"):
            response = "1"
            goodInput = True
        elif (response == "Q"
              or response == "Quit"
              or response == "q"
              or response == "quit"
              or response == "X"
              or response == "Exit"):
              response = "Q"
              goodInput = True   
        elif (response == "2"
              or  response == "two"
              or  response == "Two"):
                  response = "2"
                  goodInput = True 
        elif (response == "4"
              or  response == "four"
              or  response == "Four"):
                  response = "4"
                  goodInput = True 
        else:
            print "Please make a valid choice"
    return response
    
def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        goodInput = True
        for character in word:
            if character not in nums:
                print "not a number"
                goodInput = False
                break
        if goodInput and (int(word) < minNumber or int(word) > maxNumber):
            goodInput = False
            print "Out of Range"
        
            
    return word

def getPet(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        PetTypes = ["dog", "cat", "fish", "bird", "hamster", "gerbil", "snake"]
        goodInput = True
        if word not in PetTypes:
            print "Not a pet"
            goodInput = False
        
    return word
    
def getHousePart(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        PartTypes = ["door", "wall", "window", "ceiling", "door frame", "head beam", "walls"]
        goodInput = True
        if word not in PartTypes:
            print "Not a part of a house"
            goodInput = False
        
    return word
    
def getZooAnimal(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        zooAnimals = ["zebra", "lion", "tiger", "rhino", "monkey", "elephant", "seal"]
        goodInput = True
        if word not in zooAnimals:
            print "Not found in a zoo"
            goodInput = False
        
    return word
        
def isSwear(word):
    swearList = ["shit",
                "piss",
                "fuck",
                "cunt",
                "ass",
                "asshole",
                "bitch",
                "cock", 
                ]
    if word in swearList:
        return True
    else:
        return False
