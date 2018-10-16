#~Easter Egg
import time    

def printPi():
    print ("It's pi time")
    time.sleep(1)
    
    f = open("pi_dec_1m.txt", "r")

    file_contents = f.read()
    f.close()


    return file_contents
