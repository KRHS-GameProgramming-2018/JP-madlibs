from screens import *
from getInput import *
import story1
import story2
import story4
import storyJake

print showSplash()
raw_input("Press Enter to Start ")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        print showSure()
        response = raw_input("Are you sure you want to quit?   ")
        if response.upper() == "Y":
            go = False
            print showQuit()
    
    # ~ elif response == "1":
        # ~ print story1.playMadlibs()
        # ~ raw_input("Press Enter to Continue")
    elif response == "1":
        print story2.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "2":
        print storyJake.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "3":
        print story4.playMadlibs()
        raw_input("Press Enter to Continue")
    else:
        print "OMG Got invalid menu option!!!"
        
        from screens import *
