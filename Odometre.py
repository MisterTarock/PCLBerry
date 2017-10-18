import RPi.GPIO as GPIO
import time
from Ultrason import *
from stop import *
from MotorControl import *
from math import *

class Odo:
    def __init__(self):

        self.Done=False
        self.Turning=True
		#to define whicj type of layout is used for the pin mapping
        GPIO.setmode(GPIO.BOARD)

        self.OdoL = 23
        self.OdoD = 21
        self.FirsTime=False
        GPIO.setup(self.OdoD, GPIO.IN)
        GPIO.setup(self.OdoL, GPIO.IN)
        self.L = 0
        self.LastL=0
        self.LastD=0
        self.PWMD=70
        self.D = 0

        self.sensor=Ultrason()
        self.motor=MotorControl()

        # time.sleep(0.5)
        # self.PWMD=50
        # self.motor.forward(50, self.PWMD)


    def setDistance(self,Dist):
        self.Turning=False
        wheelPerim = 7 * 3.14
        wheelTurns = Dist / wheelPerim
        clicks = wheelTurns * 20
        self.Dist = clicks
        print(self.Dist)
        self.motor.forward(70, 70)
        self.Acquisition()

    def setTurn(self,direction,radius,angle):
        self.Turning=True
        outsidePerimeter = 2 * 3.1416 * (radius + 8)
        insidePerimeter = 2 * 3.1416 * (radius - 8)
        innerDistance = (insidePerimeter / 360) * angle
        outerDistance = (outsidePerimeter / 360) * angle
        wheelPerim = 7 * 3.1416

        if direction == "left":
            wheelTurns = innerDistance/wheelPerim
            self.motor.left(innerDistance,outerDistance)
        if direction == "right":

            wheelTurns = outerDistance/wheelPerim
            self.motor.right(innerDistance,outerDistance)
        clicks = wheelTurns * 20
        self.Dist = clicks
        self.Acquisition()


    def incrementL(self,channel):
        #if GPIO.input(self.OdoL):     # if port 23 == 1
            #print ("Rising edge detected on OdoL")

        self.L+=1
        self.LastL+=1
        if self.LastL==5:
            if self.Turning==False:
                self.Regulation()
                self.LastD=0
                self.LastL=0


        if self.L>=self.Dist:
            self.Done=True
            self.motor.stop()
            time.sleep(1)

        #print ("rising="+str(self.L))


    def incrementD(self,channel):
        self.D+=1
        self.LastD+=1

    def Acquisition(self):
        print('Acquisition')
        print(self.Dist)
        print(self.L)
        if self.FirsTime==False:
            GPIO.add_event_detect(self.OdoL, GPIO.BOTH, callback=self.incrementL, bouncetime=100)
            GPIO.add_event_detect(self.OdoD, GPIO.BOTH, callback=self.incrementD, bouncetime=100)
        reset=False
        while(self.Done!=True):

            while (self.sensor.Check()):
                if self.Turning==False:
                    self.motor.stop()
                    time.sleep(2)
                    reset=True
            if reset==True:
                # self.motor.forward(90, 90)
                self.motor.forward(50,self.PWMD)
                reset=False

        print(self.L, self.D)
        self.L = 0
        self.D=0
        self.motor.stop()
        self.FirsTime=True
        self.Done=False




        return 1
        #GPIO.add_event_detect(OdoL, GPIO.FALLING, callback=incrementL)

        #GPIO.add_event_detect(self.OdoD, GPIO.BOTH, callback=self.incrementD, bouncetime=100)
        #GPIO.add_event_detect(OdoD, GPIO.FALLING, callback=incrementD)
    def CheckOdo(self):
        return self.L
    def Close(self):
        GPIO.cleanup()
    def Regulation(self):
        print(self.LastL,self.LastD)
        error=self.LastL-self.LastD
        self.PWMD+=(error/0.2)

        print("Modiying right wheel PWM to"+str(self.PWMD))
        self.motor.forward(70,self.PWMD)




odo=Odo()
odo.setDistance(10)
odo.setTurn("right",30,90)
odo.Close()