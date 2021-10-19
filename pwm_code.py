import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep # import time.sleep()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # BCM for GPIO *port* numbering
import main

def light():
  #ramp up
  #print('Registered')
  #print('switch 1')
  pwm1.start(0) 
  for dc1 in range(s1):
    pwm1.ChangeDutyCycle(dc1)
    sleep(0.01)
  pwm1.stop()
  #ramp down
  '''
  for d in range(51):
    pwm2.ChangeDutyCycle(51-d)
    sleep(0.01)
    pwm2.stop()
  '''
  #print('switch 2')
  pwm2.start(0)
  for dc2 in range(s2):
    pwm2.ChangeDutyCycle(dc2)   # set duty cycle
    sleep(0.01)
    pwm2.stop()
  '''
  #ramp down
    for d in range(51):
      pwm3.ChangeDutyCycle(51-d)
      sleep(0.01)
      pwm3.stop()
  '''
  #print('switch 3')
  pwm3.start(0)
  for dc3 in range(s3):
    pwm3.ChangeDutyCycle(dc3)   # set duty cycle
    sleep(0.01)
    pwm3.stop()




pins = {}
p1 = 4
p2 = 17
p3 = 13
GPIO.setup(p1, GPIO.OUT) 
GPIO.setup(p2, GPIO.OUT) 
GPIO.setup(p3, GPIO.OUT)
f = 1000 # frequency (Hz)
dc = 50 # duty cycle (%)
pwm1 = GPIO.PWM(p1,f)
pwm2 = GPIO.PWM(p2,f)
pwm3 = GPIO.PWM(p3,f)