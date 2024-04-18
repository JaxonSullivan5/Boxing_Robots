###Imports Class To Change Score
from scoreboardClass import Scores

###Imports For Pins
import RPi.GPIO as GPIO

###Imports For Delays
from time import sleep

###Setups Board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

###Makes Varuables

#Variable To Make Button-Like
same=False

#Score Variable
s=0

###Setups Pin

#Input Pin
GPIO.setup(14, GPIO.IN)

#Scoreboard Variable
score=Scores(26, 19, 13, 21, 20, 16, 12)

#Sets Scoreboard To 0
score.update(s)

same=False

#Score Variable
s=0

###Setups Pin

#Input Pin
GPIO.setup(14, GPIO.IN)

#Scoreboard Variable
score=Scores(26, 19, 13, 21, 20, 16, 12)

#Sets Scoreboard To 0
score.update(s)

###Delay Between Startup
print('Initializing...')
sleep(3)

###Makes The Score Update Only Once When 1
try:
        while True:

#Gets Input of Pin 14
                x=GPIO.input(14)

#If Button Pressed And Not Updated Yet
                if x==1 and same==False:
                        s=s+1
                        score.update(s)
                        print('Change')
                        same=True

#If Button Pressed And Updated Already
                elif x==1 and same==True:
                        print('Reset Please')

#Button Is Released
                elif x==0 and same==True:
                        same=False
                        print('Ready')

#Waiting For Button To Be Pressed
                else:
                        print('Waiting For Update')

#Changes Score Back To 0 If Surpasses 9
                if s>=9:
                        s=-1

#Resets 1/0 Variable
                x=0

###Stops Program
except KeyboardInterrupt:
        GPIO.cleanup()
