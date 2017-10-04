import RPi.GPIO as GPIO
from time import sleep

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

print("Turning motor Avant on")
GPIO.output(Motor1Arr, GPIO.LOW)
GPIO.output(Motor1Av, GPIO.HIGH)
GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor2Arr, GPIO.LOW)
GPIO.output(Motor2Av, GPIO.HIGH)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(20)

print("Turning motor Arrière on")
GPIO.output(Motor1Arr, GPIO.HIGH)
GPIO.output(Motor1Av, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor2Arr, GPIO.HIGH)
GPIO.output(Motor2Av, GPIO.LOW)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(20)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)
GPIO.output(Motor2Arr, GPIO.LOW)
GPIO.output(Motor2E, GPIO.LOW)

GPIO.cleanup()
