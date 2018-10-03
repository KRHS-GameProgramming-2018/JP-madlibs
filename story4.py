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
    output += "One lovely " + day1
    output += " morning my friend, " + friend1
    output += ", and I were walking down the streets of " + kearsargeTown
    output += " looking for something to do and not finding."
    output += " Suddenly, we saw " + friend2
    output += " As we got closer we felt something was off."
    output += ' when we got close enough we saw a dig green booger dripping out of his nose "' + interjection
    output += ' you look awful!" '
    output += '"Im sick, I have had this cold for a week and its not getting any better! " said ' + friend2
    output += ". We ask" + friend2
    output += " if he wanted to join our search for something to do but he declined."
    output += " We continued walking around " + kearsargeTown
    output += " for " + numHours1
    output += " hours until we saw a Zoo right outside of town! We spent " + numHours2
    output += " looking at the different animals and amusment " 
    output += "but, my favorite was looking at the " + zooAnimals
    output += "."
    
    return output
