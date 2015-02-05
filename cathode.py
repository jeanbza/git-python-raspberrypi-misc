import RPi.GPIO as GPIO
import time
import sys

if len(sys.argv) < 2:
    print "1 argument required: # cycles"
    sys.exit(1)

cycles = int(float(sys.argv[1]))

GPIO.setmode(GPIO.BCM)

blue_pin = 5
green_pin = 6
red_pin = 13

uptime = .05

pins = [blue_pin, green_pin, red_pin]

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

def unique_arr_sum(arr):
    sum = 0
    previous_items = [] # To avoid things like [15, 15] being counted
                        # differently than [15]

    for i in arr:
        if i not in previous_items:
            previous_items.append(i)
            sum += i

    return sum

def lightup(pins, uptime):
    if unique_arr_sum(pins) not in lit_pins:
        print "Outputting: ", pins, " whose unique id is ", unique_arr_sum(pins)

        lit_pins.append(unique_arr_sum(pins))

        for pin in pins:
            GPIO.output(pin, 1)
    
        time.sleep(uptime)
    
        for pin in pins:
            GPIO.output(pin, 0)
    
        time.sleep(uptime)

try:
    for x in range(cycles):
        lit_pins = []

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
