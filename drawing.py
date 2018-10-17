#Jake cardillo-Drawing-Radioactive Symbol
from shapes_new import *



def center(t, size=10):
    arc(t, size*2)
def wing (t, size = 10, rotate=0):
    t.lt(rotate)
    move(t, size*3,0)
    line(t,size*7,0)
    move(t , -size *10 ,0)
    arc(t, size*3, 60, 120)
    arc(t, size*10, 60, 120)
    t.lt(60)
    move(t, size*3, 0)
    line(t, size *7,0)
    move(t, size * -10, 0)
    t.rt(60)
    t.rt(rotate)    
def outside (t, size = 10):
    arc(t, size*11)
def symbol (t,size = 10):
    center(t, size)
    angle = 0
    wings = 0
    while wings < 3:
        wing(t,size, angle)
        wings += 1
        angle += 120
    outside(t, size)


def tree(t, size = 25, angle = 45, minsize= 1):
    if size > minsize:
      t.fd(size)
      t.lt(angle)
      tree(t, size/2, angle, minsize)
      t.rt(angle*2)
      tree(t, size/2, angle, minsize)
      t.lt(angle)
      t.bk(size)
    else:
        return
        

def serptri (t, size= 25, minsize = 15):
    if size > minsize:
        equilateral_tri(t,size)
        move(t, size/2, 0)
        equilateral_tri(t, size/2)
        #serptri(t, size/2, minsize)
        move(t, size/-4, size/2.285)
        #serptri(t, size/2, minsize)
        equilateral_tri(t, size/2)
        equilateral_tri(t, size/2, 240)
        t.x=0
        t.y=0
        serptri(t, size/2, minsize)
    else:
        return
    
#-------Test------#



