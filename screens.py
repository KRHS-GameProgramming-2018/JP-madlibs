import time,random

def showSplash():
    output = ""
    output += "---------------------------------------\n"
    output += "|                                     |\n"
    output += "|              MADLIBS                |\n"
    output += "|                 by                  |\n"
    output += "|           Jake and Peter            |\n"
    output += "|                                     |\n"
    output += "---------------------------------------\n"

    
    return output
    
def showMenu():
    output = ""
    output += "---------------------------------------\n"
    output += "|                                     |\n"
    output += "|Main Menu:                           |\n"
    output += "|   1) A Crazy Holiday                |\n"
    output += "|   2) Randy's Commute                |\n"
    output += "|   3) Peter's story                  |\n"
    output += "|   Q) Quit                           |\n"
    output += "|                                     |\n"
    output += "---------------------------------------\n"

    
    return output


def showSure():
    output = ""
    output += "---------------------------------------\n"
    output += "|                                     |\n"
    output += "|   Are you sure you want to quit?    |\n"
    output += "|                                     |\n"
    output += "|    Yes                 No           |\n"
    output += "|    (Y)                (N)           |\n"
    output += "|                                     |\n"
    output += "|                                     |\n"
    output += "---------------------------------------\n"

    
    return output


def showQuit():
    output = ""
    output += "---------------------------------------\n"
    output += "|                                     |\n"
    output += "|               Thanks                |\n"
    output += "|                for                  |\n"
    output += "|              playing!               |\n"
    output += "|                                     |\n"
    output += "---------------------------------------\n"

    
    return output
    
    
    
def showEgg():
    items = [unichr(i) for i in range(0x30a1,0x30ff + 1)]

    for i in range(1,11): # spaces and numbers
        items.append(str(i))
        items.append(" "*i)
    
    row = 30
    column= 120
    
    output = ""
 
    for i in range(row): #for every row
        s = ''      #new string
        for j in range(column): #for every column (or character)
            ri = random.randrange(len(items)) #random index
            s += items[ri]

        output += s + "\n"

    
    return output
    
