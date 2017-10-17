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
        self.LastL=0
        self.LastD=0
        self.PWMD=0.5
        self.D = 0
        self.Dist=Dist
        print(self.Dist)
        self.sensor=Ultrason()
        self.motor=MotorControl()
        self.motor.forward(1,0.5)
        self.Acquisition()





    def incrementL(self,channel):
        #if GPIO.input(self.OdoL):     # if port 23 == 1
            #print ("Rising edge detected on OdoL")
        self.L+=1
        self.LastL+=1
        if self.LastL==5:
            self.Regulation()
            self.LastD=0
            self.LastL=0

        if self.L>=self.Dist:
            self.Done=True
            self.motor.stop()
            time.sleep(1)

            self.Close()
        #print ("rising="+str(self.L))


    def incrementD(self,channel):
        self.D+=1
        self.LastD+=1

    def Acquisition(self):
        print('Acquisition')
        GPIO.add_event_detect(self.OdoL, GPIO.BOTH, callback=self.incrementL, bouncetime=100)
        GPIO.add_event_detect(self.OdoD, GPIO.BOTH, callback=self.incrementD, bouncetime=100)
        reset=False
        while(self.Done!=True):

            while self.sensor.Check():

                self.motor.stop()
                time.sleep(2)
                reset=True
            if reset==True:
                self.motor.forward(0.5,self.PWMD)
                reset=False

        print(self.L, self.D)
        self.L = 0
        self.D=0
        self.motor.stop()

        GPIO.cleanup()
        return 1
        #GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

        #GPIO.add_event_detect(self.OdoD, GPIO.BOTH, callback=self.incrementD, bouncetime=100)
        #GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)
    def CheckOdo(self):
        return self.L
    def Close(self):
        print(self.L, self.D)
        GPIO.cleanup()
    def Regulation(self):
        print(self.LastL,self.LastD)
        error=self.LastL-self.LastD
        self.PWMD+=(error/0.2)/100

        print("Modiying right wheel PWM to"+str(self.PWMD))
        self.motor.forward(0.5,self.PWMD)




Odo(100)
