###Imports Scoreboard Class
from scoreboardClass import Scores

###Imports Sleep
from time import sleep

###Imports RPi.GPIO
import RPi.GPIO as GPIO

###GPIO Pin Variables

#GPIO Pin One
p1=6

#GPIO Pin Two
p2=5

###Setsup Board & GPIO Pin

#Sets Board To BCM
GPIO.setmode(GPIO.BCM)

#Makes Pin One Input Pin
GPIO.setup(p1, GPIO.IN)

#Makes Pin Two Input Pin
GPIO.setup(p2, GPIO.IN)

###Makes Scoreboard Variabless

#Scoreboard Variable One
scoreOne=Scores(26, 19, 13, 21, 20, 16, 12)

#Scoreboard Variable Two
scoreTwo=Scores(7, 8, 25, 24, 23, 18, 15)

###Score Variables

#Score For Scoreboard One
x=0

#Score For Scoreboard Two
y=0

###Time Variable
t=0

###Inital Button Press Variables

#Button One Intially Pressed Variable
same1=False

#Button Two Initially Pressed Variable
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

#Checks For Initial Button Press
        if same2==False and GPIO.input(p2)==1:

#Updates Score Of Button Two
                y=y+1
                scoreTwo.update(y)

#Updates Initial Press Variable
                same2=True

###Second Button Is Released

#Checks When Button Two Is Released
        elif GPIO.input(p2)==0 and same2==True:

#Resets Initial Butto Press Variable Of Button Two
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
