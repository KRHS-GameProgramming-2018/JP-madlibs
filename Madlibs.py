from screens import *
from getInput import *
import story1
import story2
import story4
import storyJake

print showSplash()
raw_input("Press Enter to Start")

go = True
while go:
    print showMenu()
    response = getMenuInput()
    if response == "Q":
        #go = False
        #print showSure():
         #   if response == "Y":
                print showQuit()
          #  elif response == "N":
           #     print showMenu ()
        
    elif response == "1":
        print story1.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "2":
        print story2.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "3":
        print storyJake.playMadlibs()
        raw_input("Press Enter to Continue")
    elif response == "4":
        print story4.playMadlibs()
        raw_input("Press Enter to Continue")
    else:
        print "OMG Got invalid menu option!!!"
        
        from screens import *
