from scoreboardClass import Scores
from time import sleep
import RPi.GPIO as GPIO


p=6
GPIO.setmode(GPIO.BCM)
GPIO.setup(p, GPIO.IN)
scoreOne=Scores(26, 19, 13, 21, 20, 16, 12)
scoreTwo=Scores(7, 8, 25, 24, 23, 18, 15)
x=0
t=0
same=False

while True:
        if same==False and GPIO.input(p)==1:
                print(GPIO.input(p))
                x=x+1
                scoreOne.update(x)
                scoreTwo.update(x)
                same=True
                #print(x)

        elif GPIO.input(p)==0 and same==True:
                same=False

        scoreOne.on()
        scoreTwo.off()
        sleep(t)

        scoreOne.off()
        scoreTwo.on()
        sleep(t)

        if x>=9:
                x=-1
