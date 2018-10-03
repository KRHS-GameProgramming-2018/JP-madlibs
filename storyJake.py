from getInput import *


def playMadlibs():
    friend1 = getFriend("Enter a Name: ")
    numAnimals = getNumber("Enter a number: ", 2, 100000)
    animals1 = getWord("Enter a pluaral animal name: ")
    dayWeek = getDay ("Enter a day of the week: ")
    food = getWord ("Enter a food: ")
    city = getWord ("Enter a city: ")
    noun = getWord (" Enter a noun: ")
    
    
    
    
    output = " "
    output += " I woke up groggy and still tired, it was just a normal " + dayWeek
    output += " morning. " " I went downstairs made myself a nice big breakfast of " + food 
    output += "." " I had to rush, traffic was probably gonna be pretty bad, like it is every morning in "  + city 
    output += "." " My commute to work at the " + noun
    output += " factory was going smoothly, until I had to pull onto the freeway. " " The traffic didn't seem too bad at first, but I suddenly got a text from my coworker " +friend1 
    output += ", 'Hey Randy, watch out up by exit 23', they say. " " I got worried, traffic was always bad, no reason to warn someone about it, especially not coming from the calm, cool, and collected " +friend1
    output += "." " I was only about a mile from work when a stampede of what must have been " + numAnimals 
    output += " " + animals1
    output += " rushed across the road! " " I was amazed, guess it wasn't just some normal " + dayWeek 
    output += " in " +city
    

    
    return output
    
 
