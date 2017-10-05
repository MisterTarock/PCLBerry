import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

TRIG= 26  #to send the ultrasonic pulse
ECHO= 24  #to mesure the distance from the obstacle and give it as a 5V impluse

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO)==0:
  pulse_start = time.time()

while GPIO.input(ECHO)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start #to mesure the time of the ECHO

distance = pulse_duration * 17150
distance = round(distance, 2)

print "Distance:",distance,"cm"

GPIO.cleanup()
