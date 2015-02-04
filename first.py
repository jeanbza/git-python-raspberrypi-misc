import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)

count = 0
light_time = .2
flashes = 20

while count < flashes:
  GPIO.output(led_pin, 1)
  time.sleep(light_time)
  GPIO.output(led_pin, 0)
  time.sleep(light_time)
  count += 1

GPIO.cleanup()
