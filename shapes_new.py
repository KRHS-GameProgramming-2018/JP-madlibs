from TurtleWorld import *
from math import *

#-------------------------OTHER FUNCTIONS-------------------------#
  
def law_of_cosines(adj1, adj2, opp):
  ang=degrees(acos(((adj1**2)+(adj2**2)-(opp**2))/(2*adj1*adj2)))
  return ang
  
#----------------------------TRIANGLES----------------------------#
 
def equilateral_tri(turtle, size=100, rotate=0):
    print "Equilateral Triangle, with Size:", size, "and Rotation:", rotate
    tri(turtle, size, size, size, rotate)
  
def right_tri(turtle, base=100, height=50, rotate=0):
    print "Right Triangle, with Base:", base, "Height:", height, "and Rotation:", rotate
    hyp=sqrt((base*base)+(height*height))
    tri(turtle, base, height, hyp, rotate) 

def sss_tri(turtle, side1=100, side2=50, side3=75, rotate=0):
    print "SSS Triangle, with Sides:", side1, side2, side3, "and Rotation:", rotate
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]>sides[0]+sides[1]:
        print "\tBad Triangle!"
        return
    turtle.lt(rotate) 
    side1=float(side1)
    side2=float(side2)
    side3=float(side3)
    ang1=180-law_of_cosines(side1, side2, side3)
    ang2=180-law_of_cosines(side2, side3, side1)
    ang3=180-law_of_cosines(side1, side3, side2)
    turtle.fd(side1)                         
    turtle.lt(ang1)
    turtle.fd(side2)
    turtle.lt(ang2)
    turtle.fd(side3)
    turtle.lt(ang3)  
    turtle.rt(rotate) 
    
def tri(turtle, side1=100, side2=50, side3=75, rotate=0):
    sss_tri(turtle, side1, side2, side3, rotate)
    
#--------------------------QUADRILATERALS-------------------------#

def para(turtle, width=100, height=100, big_angle=120, rotate=0):
    print "Parallelogram, with Width:", width, "Height:", height, "Large Angle:", big_angle, "and Rotation:", rotate
    small_angle=180-big_angle
    turtle.lt(rotate)
    turtle.fd(width)
    turtle.lt(small_angle)
    turtle.fd(height)
    turtle.lt(big_angle)
    turtle.fd(width)
    turtle.lt(small_angle)
    turtle.fd(height)
    turtle.lt(big_angle)
    turtle.rt(rotate) 

def rhom(turtle, size=100, big_angle=120, rotate=0):
    print "Rhombus, with Size:", size, "Large Angle:", big_angle, "and Rotation:", rotate
    para(turtle, size, size, big_angle, rotate)
  
def rect(turtle, width=100, height=100, rotate=0):
    print "Rectangle, with Width:", width, "Height:", height, "and Rotation:", rotate
    para(turtle, width, height, 90, rotate)

def square(turtle, size=100, rotate=0):
    print "Sqaure, with Size:", size, "and Rotation:", rotate
    para(turtle, size, size, 90, rotate)
  
#-------------------------------POLYGONS--------------------------#

def poly(turtle, sides=5, size=100, rotate=0):
    print "Polygon, with Sides:", sides, "Size:", size, "and Rotation:", rotate
    turtle.lt(rotate)
    angle = 360.0/sides
    count=1
    while count<=sides:
        turtle.fd(size)
        turtle.lt(angle)
        count+=1
    turtle.rt(rotate) 

def star(t, points=5, size=100.0, rotate=0):
    #Based on function by zander blasingame
    print "Star, with Points:", points, "Size:", size, "and Rotation:", rotate
    t.lt(rotate)
    for i in range(points):
            t.fd(side)
            t.rt(720/float(points))
    t.rt(rotate)   

#------------------------------MOVEMENT---------------------------#

def line(turtle, x=100, y=100):
    print "Line to a point X:", x, "over and Y:", y, "up"
    x=float(x)
    y=float(y)
    if x!=0 and y!=0: #Not on an Axis
        hyp=sqrt(x**2+y**2)
        angle=degrees(atan(y/x))
    elif x==0: #On X Axis
        angle=90
        hyp=y
    else:   #On Y Axis
        angle=0
        hyp=x
        
    if x<0 and y<0: #Quad 3
        angle=angle-180
    elif x<0 and y>0: #Quad 2
        angle=angle+180
    elif x>0 and y<0: #Quad 4
        angle=angle

    turtle.lt(angle)
    turtle.fd(hyp)
    turtle.lt(360-angle)    
  
def move(turtle, x, y):
    print "Move without marking a line to a point X:", x, "over and Y:", y, "up"
    turtle.pu()
    line(turtle, x, y)
    turtle.pd()
 
#-----------------------------Arc---------------------------#

def arc(turtle, radius, angle=360, rotate=0):
    radius=float(radius)
    angle=float(angle)
    print "Arc, with Radius Size:", radius, "Angle of Arc:", angle, "and Rotation:", rotate
    coor=(turtle.x,turtle.y) #Needed to prevent turtle from drifting
    turtle.rt(rotate)
    #---Move Turtle---
    turtle.pu()
    turtle.bk(radius)
    turtle.lt(90)
    turtle.pd()
    #---Draw Arc---
    arcLength=2*pi*radius*angle/360
    sides=int(arcLength/3)+1
    stepLength=arcLength/sides
    stepAngle=float(angle)/sides
    totalAngle=0
    for side in range(sides):
        fd(turtle, stepLength)
        rt(turtle, stepAngle) 
        totalAngle+=stepAngle  
    #---Move Turtle Back---
    turtle.pu()
    turtle.rt(90)
    #turtle.fd(radius)
    (turtle.x,turtle.y)=coor 
    turtle.pd()
    turtle.lt(totalAngle)
    turtle.lt(rotate)

