###Imports Scoreboard Class
from scoreboardClass import Scores

###Imports Sleep
from time import sleep

###Imports RPi.GPIO
import RPi.GPIO as GPIO

###GPIO Pin Variable
p1=6
p2=5

###Setsup Board & GPIO Pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(p1, GPIO.IN)
GPIO.setup(p2, GPIO.IN)

###Makes Scoreboard Variables
scoreOne=Scores(26, 19, 13, 21, 20, 16, 12)
scoreTwo=Scores(7, 8, 25, 24, 23, 18, 15)

###Score Variable
x=0
y=0

###Time Variable
t=0

###Button Press Variable
same1=False
same2=False

###Loop
while True:

###First Button Is Pressed
        if same1==False and GPIO.input(p1)==1:
                x=x+1
                scoreOne.update(x)
                same1=True

###First Button Is Released
        elif GPIO.input(p1)==0 and same1==True:
                same1=False

###Second Button Is Pressed
        if same2==False and GPIO.input(p2)==1:
                y=y+1
                scoreTwo.update(y)
                same2=True

###Second Button Is Released
        elif GPIO.input(p2)==0 and same2==True:
                same2=False

###Multiplexes Board (So it doesn't draw too much power)
        scoreOne.on()
        scoreTwo.off()
        sleep(t)

        scoreOne.off()
        scoreTwo.on()
        sleep(t)

###Resets X (Button 1) To 0
        if x>=9:
                x=-1

###Resets Y (Button 2) To 0
        if y>=9:
                y=-1
