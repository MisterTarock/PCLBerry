import RPi.GPIO as GPIO
import time
#to define whicj type of layout is used for the pin mapping
GPIO.setmode(GPIO.BOARD)

OdoL= 23
OdoD= 21

GPIO.setup(OdoD, GPIO.IN)
GPIO.setup(OdoL, GPIO.IN)

def incrementL(channel):
    L=0
    if GPIO.input(OdoL):     # if port 23 == 1
        print "Rising edge detected on OdoL"
        L=L+1
        print L
    else:                  # if port 23 != 1
        print "Falling edge detected on OdoL"

def incrementD(channel):
    if GPIO.input(OdoD):     # if port 21 == 1
        print "Rising edge detected on OdoD"
    else:                  # if port 21 != 1
        print "Falling edge detected on OdoD"

def Acquisition():
    print('Acquisition')
    GPIO.add_event_detect(OdoL, GPIO.RISING, callback=incrementL)
    #GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

    GPIO.add_event_detect(OdoD, GPIO.RISING, callback=incrementD)
    #GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)


Acquisition()
sleep(2)


GPIO.cleanup()
