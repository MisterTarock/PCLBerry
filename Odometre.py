import RPi.GPIO as GPIO
import time
from MotorControl import *
#to define whicj type of layout is used for the pin mapping

class Odo:
    def __init__(self,Dist):
        self.Done=False
        GPIO.setmode(GPIO.BOARD)

        self.OdoL = 23
        self.OdoD = 21

        GPIO.setup(self.OdoD, GPIO.IN)
        GPIO.setup(self.OdoL, GPIO.IN)
        self.L = 0
        self.Dist=Dist
        motor=MotorControl()
        motor.forward()
        self.Acquisition()



    def incrementL(self,channel):
        #if GPIO.input(self.OdoL):     # if port 23 == 1
            #print ("Rising edge detected on OdoL")
        self.L+=1
        if self.L>=self.Dist:
            self.Done=True


        print ("rising="+str(self.L))
        #else:                  # if port 23 != 1
        #    print ("Falling edge detected on OdoL")

    def incrementD(self,channel):

        if GPIO.input(self.OdoD):     # if port 21 == 1
             print ("Rising edge detected on OdoD")
        else:                  # if port 21 != 1
            print ("Falling edge detected on OdoD")

    def Acquisition(self):
        print('Acquisition')
        while(self.Done!=True):


            GPIO.add_event_detect(self.OdoL, GPIO.BOTH, callback=self.incrementL, bouncetime=100)
        self.L = 0
        MotorControl.stop()
        GPIO.cleanup()
        return 1
        #GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

        #GPIO.add_event_detect(self.OdoD, GPIO.BOTH, callback=self.incrementD, bouncetime=100)
        #GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)
    def CheckOdo(self):
        return self.L


Odo(100)
