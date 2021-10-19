#!/usr/bin/cgipython1
import cgi
import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep # import time.sleep()
GPIO.setwarnings(False)
import json
import cgitb
cgitb.enable()
import pwm.html

def light():
  #ramp up
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

print("Content-type: text/html\n\n")
data= cgi.FieldStorage()
print("s1 = " + data.getvalue('slider1') + '<br>')
print("s2 = " + data.getvalue('slider2') + '<br>')
print("s3 = " + data.getvalue('slider3'))

s1 = data.getvalue('slider1')
s2 = data.getvalue('slider2')
s3 = data.getvalue('slider3')
data = {"slider1":s1, "slider2":s2, "slider3":s3}
with open('led-pwm-multiple.txt', 'w') as f:
  json.dump(data,f)
with open('led-pwm-multiple.txt', 'r') as f:
  data = json.load(f)
print("slider 1 = "+ str(data['slider1']))
print("slider 2 = "+ str(data['slider2']))
print("slider 3 = "+ str(data['slider3']))
light()