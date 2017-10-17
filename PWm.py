import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
Motor1Av = 18
Motor2Av = 16
GPIO.setup(Motor1Av, GPIO.OUT)
GPIO.setup(Motor2Av, GPIO.OUT)
M1For = GPIO.PWM(Motor1Av, 100)
M2For = GPIO.PWM(Motor1Av, 100)
print("turning on")
M1For.ChangeDutyCycle(0.5)
M2For.ChangeDutyCycle(0.5)
time.sleep(5)
print("maxing")
M1For.ChangeDutyCycle(1)
M2For.ChangeDutyCycle(1)

time.sleep(2)
print("turning off")
M1For.ChangeDutyCycle(0)
M2For.ChangeDutyCycle(0)
time.sleep(5)
GPIO.cleanup()