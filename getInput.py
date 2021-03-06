import screens
import sys
import EasterEgg

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
        elif (response == "3"
            or response == "three"
            or response == "Three"):
                response = "3"
                goodInput = True
        elif (response == "4"
              or  response == "four"
              or  response == "Four"):
                  response = "4"
                  goodInput = True 
        elif (response == "3.14"
              or response == "pi"):
                response = "3.14"
                goodInput = True
        else:
            print "Please make a valid choice"
    return response
    
def checkQuit(word):
    if word == "Quit".lower():
        print screens.showSure()
        response = raw_input("Are you sure you want to quit?   ")
        if response.upper() == "Y":
            print screens.showQuit()
            sys.exit()
        
        
        
def checkPlural(Word):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
        
        if word[-1] != "s":
            goodInput = False
        else:
            print "Not plural"
        
    return word
    
    

def getWord(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        if word.lower() == "pylon" or word.lower() == "pylons":
            print "You must construct addtional pylons!"
            print screens.showPylons()                          # Maybe this could be a function by itself; so you wouldn't have to duplicate this code so many times.
            sys.exit()
        if not isSwear(word):
            goodInput = True
        else:
            print "Watch your language!"
    return word
    
def getNumber(prompt, minNumber, maxNumber):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt+" (Between " + str(minNumber) +  " and " + str(maxNumber) + ") ")
        checkQuit(word)
        if word == ("3.14"):
            print EasterEgg.printPi()
            goodInput = True
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
        checkQuit(word)
        PetTypes = ["dog", 
                    "cat", 
                    "fish",
                    "bird", 
                    "hamster", 
                    "gerbil", 
                    "snake",
                    "lizard"]
        if word.lower() == "pylon" or word.lower() == "pylons":
            print "You must construct addtional pylons!"
            print screens.showPylons()
            sys.exit()
        goodInput = True
        if word.lower() not in PetTypes:
            print "Not a pet"
            goodInput = False
        
    return word
    
def getHousePart(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        PartTypes = ["door", 
                     "wall", 
                     "window", 
                     "ceiling", 
                     "door frame", 
                     "head beam", 
                     "walls",
                     "roof"]
        if word.lower() == "pylon" or word.lower() == "pylons":
            print "You must construct addtional pylons!"
            print screens.showPylons()
            sys.exit()
        
        goodInput = True
        if word.lower() not in PartTypes:
            print "Not a part of a house"
            goodInput = False
        
    return word
    
def getTown(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        Towns = ["warner", 
                 "sutton", 
                 "new london", 
                 "wilmot", 
                 "springfield", 
                 "newbury", 
                 "bradford"]
        if word.lower() == "pylon" or word.lower() == "pylons":
            print "You must construct addtional pylons!"
            print screens.showPylons()
            sys.exit()
        goodInput = True
        if word.lower() not in Towns:
            print "Not a town in Kearsarge"
            goodInput = False
        
    return word
    
def getZooAnimal(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        zooAnimals = ["zebras", 
                      "lions", 
                      "tigers", 
                      "rhinos",
                      "bears", 
                      "monkeys", 
                      "elephants", 
                      "seals"]
        if word.lower() == "pylon" or word.lower() == "pylons":
            print "You must construct addtional pylons!"
            print screens.showPylons()
            sys.exit()
        goodInput = True
        if word.lower() not in zooAnimals:
            print "Not found in a zoo"
            goodInput = False
        
    return word

    
def getDay (prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        if word.lower() == "pylon" or word.lower() == "pylons":
            print "You must construct addtional pylons!"
            print screens.showPylons()
            sys.exit()
        goodInput = True
        if word.lower() not in days:
            print "Not a day"
            goodInput = False
    return word
        
def getFriend(prompt):
    goodInput = False
    while not goodInput:
        word = raw_input(prompt)
        checkQuit(word)
        bannedNames = ["randy"]
        if not isSwear(word.lower()):
            goodInput = True
        else:
            print "Watch your language!"
        
        if word.lower() not in bannedNames:
            goodInput = True
        else:
            print "Don't Use that Name"
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
                "fucks",
                "cunts",
                "shits",
                "bitches",
                "cunts",
                "asses",
                "fucker",
                "dick",
                "penis",
                "hell",
                "dildo",
                "fag",
                "faggot",
                "fucked",
                 
                ]
    words = word.split()
    for w in words:
        if w.lower() in swearList:
            return True
    return False
