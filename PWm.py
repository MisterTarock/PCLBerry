import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
Motor1Av = 18
Motor2Av = 12
GPIO.setup(Motor1Av, GPIO.OUT)
GPIO.setup(Motor2Av, GPIO.OUT)
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