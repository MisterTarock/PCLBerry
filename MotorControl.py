import RPi.GPIO as GPIO
import time


class MotorControl:
    def __init__(self):
		#to define which type of layout is used for the pin mapping
        GPIO.setmode(GPIO.BOARD)

        self.Motor1Arr = 16
        self.Motor1Av = 18
        self.Motor1E = 22
        self.Motor2E = 15
        self.Motor2Arr = 13
        self.Motor2Av = 11

        GPIO.setup(self.Motor1Arr, GPIO.OUT)
        GPIO.setup(self.Motor1Av, GPIO.OUT)
        GPIO.setup(self.Motor1E, GPIO.OUT)
        GPIO.setup(self.Motor2Arr, GPIO.OUT)
        GPIO.setup(self.Motor2Av, GPIO.OUT)
        GPIO.setup(self.Motor2E, GPIO.OUT)
        self.M1For = GPIO.PWM(self.Motor1Av, 100)
        self.M2For = GPIO.PWM(self.Motor2Av, 100)
        self.M1Bac = GPIO.PWM(self.Motor1Arr, 100)
        self.M2Bac = GPIO.PWM(self.Motor2Arr, 100)
    def forward(self,LPWM,RPWM):
        print("Turning motor Forward")

        self.M1Bac.ChangeDutyCycle(0)
        self.M1For.ChangeDutyCycle(LPWM)
        self.M2Bac.ChangeDutyCycle(RPWM)
        self.M2For.ChangeDutyCycle(0)
        # GPIO.output(self.Motor1Arr, GPIO.LOW)
        # GPIO.output(self.Motor1Av, GPIO.HIGH)
        # GPIO.output(self.Motor2Arr, GPIO.LOW)
        # GPIO.output(self.Motor2Av, GPIO.HIGH)
        GPIO.output(self.Motor1E, GPIO.HIGH)
        GPIO.output(self.Motor2E, GPIO.HIGH)
        print("outputs set")


    def backward(self):
        print("Turning motor Backward")
        GPIO.output(self.Motor1Arr, GPIO.HIGH)
        GPIO.output(self.Motor1Av, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)
        GPIO.output(self.Motor2Arr, GPIO.HIGH)
        GPIO.output(self.Motor2Av, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.HIGH)

    def stop(self):
        print("Stopping motor")
        GPIO.output(self.Motor1E, GPIO.LOW)
        GPIO.output(self.Motor2Arr, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.LOW)



motor=MotorControl()
motor.forward(0.5,0.5)
time.sleep(5)
motor.backward()
time.sleep(5)
motor.stop()
GPIO.cleanup()