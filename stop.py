from MotorControl import *
import RPi.GPIO as GPIO
class stopAll:
    def __init__(self):
        motor=MotorControl()
        motor.stop()
        GPIO.cleanup()