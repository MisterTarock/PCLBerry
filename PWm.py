import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
Motor1Av = 13
Motor2Av = 16
Motor1E = 22
Motor2E = 15
GPIO.setup(Motor1Av, GPIO.OUT)
GPIO.setup(Motor2Av, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)
GPIO.output(Motor1E, GPIO.HIGH)
GPIO.output(Motor2E, GPIO.HIGH)
M1For = GPIO.PWM(Motor1Av, 100)
M2For = GPIO.PWM(Motor2Av, 100)
print("turning on")
M1For.start(50)
M2For.start(50)
time.sleep(5)
print("maxing")
M1For.ChangeDutyCycle(100)
M2For.ChangeDutyCycle(100)

time.sleep(2)
print("turning off")
M1For.ChangeDutyCycle(0)
M2For.ChangeDutyCycle(0)
time.sleep(5)
GPIO.cleanup()