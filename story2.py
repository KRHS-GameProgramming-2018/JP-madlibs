from getInput import *


def playMadlibs():
    friend1 = getWord("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 10)
    animals1 = getWord("Enter a pluaral animal name: ")
    holiday = getWord ("Enter a holiday: ")
    Pet = getPet("Enter a geneiric pet: ")
    
    
    
    
    output = " "
    output += "It was a dark and stormy " + holiday
    output += "eve" " and " + friend1 
    output += " and I were watching a documentary on " + animals1 
    output += "."
    output += "Suddenly " + numAnimals 
    output += " of them jumped out of the screen " 
    output += "and" + friend1 
    output += "'s " + Pet 
    output += " went crazy. The" + animals1
    output += "chased us around the house until" 
    
    return output
