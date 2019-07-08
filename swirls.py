from turtle import * #imports python with turtle
shades = ['salmon', 'orange', 'yellow', 'palegreen', 'skyblue', 'violet', ]
#creates the list shades of the colors used below

for i in range(500): #sets up the loop 
    speed(10) #determines the speed of the pen
    pencolor(shades[i % 6]) #i%6 each color from the list shades is used alternatively
    width(i / 50 + 3) #determines the width of the pen
    forward(i) #moves the pen forward
    left(59) #angle at which the pen is turned while moving forward
