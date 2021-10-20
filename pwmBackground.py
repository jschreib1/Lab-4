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
f = 1000 # frequency (Hz)
#dc = 50 # duty cycle (%)
pwm1 = GPIO.PWM(p1,f)
pwm2 = GPIO.PWM(p2,f)
pwm3 = GPIO.PWM(p3,f)

pwm1.start(0) # start with LED off
pwm2.start(0)
pwm3.start(0)
while True:
  with open("led-pwm-multiple.txt", 'r') as f:
    data = float(json.load(f)) # read duty cycle value from file
    dc = int(data['slider1'])
    led = data['LED']
  if led == 'a': 
    pwm1.ChangeDutyCycle(dc)
  elif led == 'b':
    pwm2.ChangeDutyCycle(dc)
  elif led == 'c':
    pwm3.ChangeDutyCycle(dc)
  
  sleep(0.1)
