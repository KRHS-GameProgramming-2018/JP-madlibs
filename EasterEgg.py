#~Easter Egg
import time    
from TurtleWorld import *
from shapes_new import *
from drawing import *

def printPi():
    print ("It's pi time")
    time.sleep(1)
    
    f = open("pi_dec_1m.txt", "r")

    file_contents = f.read()
    f.close()


    return file_contents


def crossover(): # very clever!
    print ("What is this, a crossover episode?")
    time.sleep(1.5)

    world= TurtleWorld()

    bob = Turtle()
    bob.delay = 0.0001
    bob.pen_color = "black"
    symbol(bob, 15)


    wait_for_user()
