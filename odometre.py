import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

OdoL= 23 
OdoD= 21

GPIO.setup(OdoD, GPIO.IN)
GPIO.setup(OdoL, GPIO.IN)


def incrementL(channel):
    if GPIO.input(OdoL):     # if port 23 == 1
        print "Rising edge detected on OdoL"
    else:                  # if port 23 != 1
        print "Falling edge detected on OdoL"

def incrementD(channel):
    if GPIO.input(OdoD):     # if port 21 == 1
        print "Rising edge detected on OdoD"
    else:                  # if port 21 != 1
        print "Falling edge detected on OdoD"

print('Acquisition')
GPIO.add_event_detect(OdoL, GPIO.RISING, callback=incrementL)
GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

GPIO.add_event_detect(OdoD, GPIO.RISING, callback=incrementD)
GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)

GPIO.cleanup()
