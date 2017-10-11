import RPi.GPIO as GPIO
import time
#to define whicj type of layout is used for the pin mapping
GPIO.setmode(GPIO.BOARD)

OdoL= 23
OdoD= 21

GPIO.setup(OdoD, GPIO.IN)
GPIO.setup(OdoL, GPIO.IN)
L=0
def incrementL(Lnow):
    L=Lnow
    if GPIO.input(OdoL):     # if port 23 == 1
        print ("Rising edge detected on OdoL")
        L=L+1
        print (L)
    else:                  # if port 23 != 1
        print ("Falling edge detected on OdoL")

def incrementD(Dnow):
    D=Dnow
    if GPIO.input(OdoD):     # if port 21 == 1
        print ("Rising edge detected on OdoD")
    else:                  # if port 21 != 1
        print ("Falling edge detected on OdoD")

def Acquisition(L,D):
    Lnow=L
    Dnow=D
    print('Acquisition')
    GPIO.add_event_detect(OdoL, GPIO.RISING, callback=incrementL(Lnow))
    #GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

    GPIO.add_event_detect(OdoD, GPIO.RISING, callback=incrementD(Dnow))
    #GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)
L=0
D=0
Acquisition(L,D)
time.sleep(2)


GPIO.cleanup()
