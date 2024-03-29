###GPIO Pins 2,3,4,17,27,22,10,9,11 
###11 is attatced to mosfet
###Install RPLCD by typing 'sudo pip3 RPLCD'

#Imports Libraries
from RPLCD import CharLCD
import RPi.GPIO as GPIO
import time

#Sets Up Board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
readPin=GPIO.setup(11, GPIO.IN) 
x=0
y=0

try:
  while True:
    lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
    lcd.cursor_pos = (0, 0) 
    lcd.write_string(u'Hello world!')
except KeyboardInterrupt: 
    GPIO.cleanup()

lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
lcd.write_string(u'Hello world!')

