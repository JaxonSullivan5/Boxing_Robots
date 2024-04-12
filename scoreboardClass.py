###Imports Libraries
import RPi.GPIO as GPIO
from time import sleep

###Sets Up Raspberry Pi
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

###Create Class
class Scores:

###Initialization
        def __init__ (self, pin1, pin2, pin3, pin4, pin5, pin6, pin7):

###Defines Pins
                self.pin1=pin1
                self.pin2=pin2
                self.pin3=pin3
                self.pin4=pin4
                self.pin5=pin5
                self.pin6=pin6
                self.pin7=pin7
###Sets Up Pins
                GPIO.setup(self.pin1, GPIO.OUT)
                GPIO.setup(self.pin2, GPIO.OUT)
                GPIO.setup(self.pin3, GPIO.OUT)
                GPIO.setup(self.pin4, GPIO.OUT)
                GPIO.setup(self.pin5, GPIO.OUT)
                GPIO.setup(self.pin6, GPIO.OUT)
                GPIO.setup(self.pin7, GPIO.OUT)

###Update Score Function
        def update(self, num):

###Makes 0
                if num==0:
                        print(num)
                        GPIO.output(self.pin1, GPIO.HIGH)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.LOW)
                        GPIO.output(self.pin5, GPIO.HIGH)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 1
                elif num==1:
                        print(num)
                        GPIO.output(self.pin1, GPIO.LOW)
                        GPIO.output(self.pin2, GPIO.LOW)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.LOW)
                        GPIO.output(self.pin5, GPIO.LOW)
                        GPIO.output(self.pin6, GPIO.LOW)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 2
                elif num==2:
                        print(num)
                        GPIO.output(self.pin1, GPIO.LOW)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.HIGH)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.LOW)
                        print('Score Changed')

###Makes 3
                elif num==3:
                        print(num)
                        GPIO.output(self.pin1, GPIO.LOW)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.LOW)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 4
                elif num==4:
                        print(num)
                        GPIO.output(self.pin1, GPIO.HIGH)
                        GPIO.output(self.pin2, GPIO.LOW)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.LOW)
                        GPIO.output(self.pin6, GPIO.LOW)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 5
                elif num==5:
                        print(num)
                        GPIO.output(self.pin1, GPIO.HIGH)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.LOW)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.LOW)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 6
                elif num==6:
                        print(num)
                        GPIO.output(self.pin1, GPIO.HIGH)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.LOW)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.HIGH)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 7
                elif num==7:
                        print(num)
                        GPIO.output(self.pin1, GPIO.LOW)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.LOW)
                        GPIO.output(self.pin5, GPIO.LOW)
                        GPIO.output(self.pin6, GPIO.LOW)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 8
                elif num==8:
                        print(num)
                        GPIO.output(self.pin1, GPIO.HIGH)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.HIGH)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Makes 9
                elif num==9:
                        print(num)
                        GPIO.output(self.pin1, GPIO.HIGH)
                        GPIO.output(self.pin2, GPIO.HIGH)
                        GPIO.output(self.pin3, GPIO.HIGH)
                        GPIO.output(self.pin4, GPIO.HIGH)
                        GPIO.output(self.pin5, GPIO.LOW)
                        GPIO.output(self.pin6, GPIO.HIGH)
                        GPIO.output(self.pin7, GPIO.HIGH)
                        print('Score Changed')

###Failsafe
                else:
                        print('Please Enter A Valid Number')
