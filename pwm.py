#!/usr/bin/cgipython1

import cgi
import json
import cgitb
cgitb.enable()


print("Content-type: text/html\n\n")
data= cgi.FieldStorage()
s1 = data.getvalue('slider1')
s2 = data.getvalue('LED')
data = {"slider1":s1, "LED":s2}
with open('led-pwm-multiple.txt', 'w') as f:
  json.dump(data,f)

print('<html>')
print('<form action="/cgi-bin/pwm.py" method="POST">')
print('<input type="range" name="slider1" min="0" max="100" value="%s"><br>' % s1)
print('<input type="radio" name="LED" value="a" checked> LED A <br>')
print('<input type="radio" name="LED" value="b"> LED B <br>')
print('<input type="radio" name="LED" value="c"> LED C <br>')
print('<input type="submit" value="Change LED brightness">')
print('</form>')
print('dc = %s' % s1)
print('</html>')
