import RPi.GPIO as GPIO
import time
import Odometre
#to define whicj type of layout is used for the pin mapping
GPIO.setmode(GPIO.BOARD)

Motor1Arr = 16
Motor1Av = 18
Motor1E = 22
Motor2E = 15
Motor2Arr = 13
Motor2Av = 11

GPIO.setup(Motor1Arr, GPIO.OUT)
GPIO.setup(Motor1Av, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2Arr, GPIO.OUT)
GPIO.setup(Motor2Av, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

def forward():
    print("Turning motor Forward")
    GPIO.output(Motor1Arr, GPIO.LOW)
    GPIO.output(Motor1Av, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2Arr, GPIO.LOW)
    GPIO.output(Motor2Av, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    print("outputs set")


def backward():
    print("Turning motor Backward")
    GPIO.output(Motor1Arr, GPIO.HIGH)
    GPIO.output(Motor1Av, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2Arr, GPIO.HIGH)
    GPIO.output(Motor2Av, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def stop():
    print("Stopping motor")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor2Arr, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.LOW)

done=False
forward()
Odometre.Odo(20)
while done==False:
    if Odometre.CheckOdo()==20:
        stop()
        done=True
        time.sleep(2)
    time.sleep(1)
stop()
backward()
time.sleep(2)
stop()


GPIO.cleanup()
