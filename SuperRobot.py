from Movecontrol import MoveControl
import RPi.GPIO as GPIO
import sys
import time


if __name__ == '__main__':
    robot = Robot()
    try:
        robot.run()
    except KeyboardInterrupt:
        robot.stop()
        sys.exit(0)
