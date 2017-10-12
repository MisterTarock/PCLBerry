import RPi.GPIO as GPIO
import time
from Ultrason import *
from MotorControl import *


class Odo:
    def __init__(self,Dist):

        self.Done=False
		#to define whicj type of layout is used for the pin mapping
        GPIO.setmode(GPIO.BOARD)

        self.OdoL = 23
        self.OdoD = 21

        GPIO.setup(self.OdoD, GPIO.IN)
        GPIO.setup(self.OdoL, GPIO.IN)
        self.L = 0
        self.Dist=Dist
        self.sensor=Ultrason()
        self.motor=MotorControl()
        self.motor.forward()
        self.Acquisition()





    def incrementL(self,channel):
        #if GPIO.input(self.OdoL):     # if port 23 == 1
            #print ("Rising edge detected on OdoL")
        self.L+=1
        if self.L>=self.Dist:
            self.Done=True


        print ("rising="+str(self.L))


    def incrementD(self,channel):

        if GPIO.input(self.OdoD):     # if port 21 == 1
             print ("Rising edge detected on OdoD")
        else:                  # if port 21 != 1
            print ("Falling edge detected on OdoD")

    def Acquisition(self):
        print('Acquisition')
        GPIO.add_event_detect(self.OdoL, GPIO.BOTH, callback=self.incrementL, bouncetime=100)
        while(self.Done!=True):

            if self.sensor.Check():
                self.motor.stop()
                self.Done=True
        self.L = 0
        self.motor.stop()
        GPIO.cleanup()
        return 1
        #GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

        #GPIO.add_event_detect(self.OdoD, GPIO.BOTH, callback=self.incrementD, bouncetime=100)
        #GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)
    def CheckOdo(self):
        return self.L


Odo(50)
