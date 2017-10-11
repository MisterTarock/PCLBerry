from MotorControl import *
import RPi.GPIO as GPIO
motor=MotorControl()
motor.stop()
GPIO.cleanup()