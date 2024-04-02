import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN)
servoPIN = 15
GPIO.setup(servoPIN, GPIO.OUT)


p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    print(GPIO.input(18))
    if GPIO.input(18)==1:
      p.ChangeDutyCycle(10)
      time.sleep(0.1)
    else:
      p.ChangeDutyCycle(0)
      time.sleep(0.1)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()


