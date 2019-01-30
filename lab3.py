# Lab No. 3
# CTEC 121
# YOUR NAME

from graphics import *

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    pt1 = Point(400, 500)
    circle1 = Circle(pt1, 140)
    circle1.setFill("White")
    circle1.draw(win)
    pt2 = Point(400, 370)
    circle2 = Circle(pt2, 120)
    circle2.setFill("White")
    circle2.draw(win)
    pt3 = Point(400, 275)
    circle3 = Circle(pt3, 70)
    circle3.setFill("White")
    circle3.draw(win)

    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eyePoint1 = Point(375, 260)
    eye1 = Circle(eyePoint1, 40)
    eyePoint2 = Point(425, 260)
    eye2 = Circle(eyePoint2, 40)


    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose


    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat




    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline




    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()