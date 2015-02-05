import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

blue_pin = 5
green_pin = 6
red_pin = 13

uptime = .2

pins = [blue_pin, green_pin, red_pin]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def lightup(pins, uptime):
    for pin in pins:
        GPIO.output(pin, 1)
    
    time.sleep(uptime)
    
    for pin in pins:
        GPIO.output(pin, 0)
    
    time.sleep(uptime)

try:
    # Algorithms...how do they even work
    for pin1 in pins:
        lightup([pin1], uptime)
        for pin2 in pins:
            lightup([pin1, pin2], uptime)
            for pin3 in pins:
                lightup([pin1, pin2, pin3], uptime)
        
except:
    print sys.exc_info()

GPIO.cleanup()
