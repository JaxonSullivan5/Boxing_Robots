###Imports Scoreboard Class
from scoreboardClass import Scores

###Imports Sleep
from time import sleep

###Imports RPi.GPIO
import RPi.GPIO as GPIO

###GPIO Pin Variable
p=6

###Setsup Board & GPIO Pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(p, GPIO.IN)

###Makes Scoreboard Variables
scoreOne=Scores(26, 19, 13, 21, 20, 16, 12)
scoreTwo=Scores(7, 8, 25, 24, 23, 18, 15)

###Score Variable
x=0

###Time Variable
t=0

###Button Press Variable
same=False

###Loop
while True:

###Button Is Pressed
        if same==False and GPIO.input(p)==1:
                x=x+1
                scoreOne.update(x)
                scoreTwo.update(x)
                same=True

###Button Is Released
        elif GPIO.input(p)==0 and same==True:
                same=False

###Multiplexes Board (So it doesn't draw too much power)
        scoreOne.on()
        scoreTwo.off()
        sleep(t)

        scoreOne.off()
        scoreTwo.on()
        sleep(t)

###Resets Score To 0
        if x>=9:
                x=-1
