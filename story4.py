from getInput import *


def playMadlibs():
    day1 = getDay("Enter a day of the week: ")
    friend1 = getWord("Enter a Name: ")
    kearsargeTown = getTown("Enter a town in kearsarge: ")
    friend2 = getWord("Enter a Name: ")
    interjection = getWord("Enter an Interjection: ")
    numHours1 = getNumber("Enter a number: ", 2, 12)
    numHours2 = getNumber("Enter a number: ", 2, 12)
    zooAnimals = getZooAnimal("Enter a  plural Zoo Animal: ")
    
    output = " "
    output += "One " + day1
    output += " morning my friend, " + friend1
    output += ", and I were walking down the streets of " + kearsargeTown
    output += ". When we saw " + friend2
    output += ' and said "' + interjection
    output += ' you look awful!" '
    output += '"Im sick" said ' + friend2
    output += ". We continued walking for " + numHours1
    output += " hours until we saw a zoo! We spent " + numHours2
    output += " looking at the " + zooAnimals
    
    return output
