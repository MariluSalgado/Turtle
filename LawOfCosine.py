import math
from turtle import *


##Law of Cosine
def myTriangle():

    firstSide = int (input("Put the first side Length."))
    secondSide = int(input("Give me the second side Length."))
    firstAngle = int(input("Give me one angle."))
                     

    thirdSide = (pow(firstSide,2) + pow(secondSide,2)) - ((2)*(firstSide)*(secondSide)*(math.cos(math.radians(firstAngle))))
    thirdSide1 = pow(thirdSide,0.5)

    secondAngle = math.acos(((pow(secondSide,2)) - (pow(firstSide,2)) - (pow(thirdSide1,2)))/ ((-2)*(firstSide)*(thirdSide1)))
    secondAngle1 = math.degrees(secondAngle)

    thirdAngle = (180 - firstAngle - secondAngle1)


    ##TURTLE DRAWING##
    marilu = Turtle()

    marilu.goto(0,0)
    marilu.down ()
    marilu. forward (firstSide)
    marilu.left(180 - thirdAngle)
    marilu.forward(secondSide)
    marilu.left (180 - firstAngle)
    marilu.forward (thirdSide1)







print ("First Angle:")
print (firstAngle)
print ("secondAngle:")
print (secondAngle1)
print ("Thrid Angle:")
print (thirdAngle)

if __name__ == "__main__":
    myTirangle()







                     
