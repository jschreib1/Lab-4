import json
import cgi
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep # import time.sleep()
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
pins = {}
p1 = 4
p2 = 17
p3 = 13
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT)
fr = 1000 # frequency (Hz)
#dc = 50 # duty cycle (%)
pwm1 = GPIO.PWM(p1,fr)
pwm2 = GPIO.PWM(p2,fr)
pwm3 = GPIO.PWM(p3,fr)

pwm1.start(0) # start with LED off
pwm2.start(0)
pwm3.start(0)
while True:
  with open("led-pwm-multiple.txt", 'r') as f:
    data = json.load(f) # read duty cycle value from file
    dc = data['slider1']
    led = int(data['LED'])
  if led == 1: 
    pwm1.ChangeDutyCycle(int(dc))
  elif led == 2:
    pwm2.ChangeDutyCycle(int(dc))
  elif led == 3:
    pwm3.ChangeDutyCycle(int(dc))
  
  sleep(0.1)
