import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

blue_pin = 5
green_pin = 6
red_pin = 13

GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

def lightup(pin, uptime):
    GPIO.output(pin, 1)
    time.sleep(uptime)
    GPIO.output(pin, 0)
    time.sleep(uptime)

try:
    lightup(blue_pin, .2)
    lightup(green_pin, .2)
    lightup(red_pin, .2)
except:
    print "Unexpected error: ", sys.exc_info()[0]
GPIO.cleanup()
