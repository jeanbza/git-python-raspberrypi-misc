import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

count = 0
light_time = .1
flashes = 20

green_pin = 17
red_pin = 27

GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(red_pin, GPIO.OUT)

while count < flashes:
  GPIO.output(green_pin, 1)
  time.sleep(light_time)
  GPIO.output(red_pin, 1)
  time.sleep(light_time)
  GPIO.output(green_pin, 0)
  time.sleep(light_time)
  GPIO.output(red_pin, 0)
  time.sleep(light_time)
  count += 1

GPIO.cleanup()
