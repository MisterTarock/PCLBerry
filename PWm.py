import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
Motor1Av = 18
GPIO.setup(Motor1Av, GPIO.OUT)
M1For = GPIO.PWM(Motor1Av, 100)
M1For.ChangeDutyCycle(50)