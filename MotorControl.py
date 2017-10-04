import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22
Motor2E = 15
Motor2A = 13
Motor2B = 11

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

print("Turning motor on")
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor2A, GPIO.LOW)
GPIO.output(Motor2B, GPIO.LOW)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(2)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)
GPIO.output(Motor2A, GPIO.LOW)
GPIO.output(Motor2E, GPIO.LOW)

GPIO.cleanup()