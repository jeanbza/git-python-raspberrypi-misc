import time
import RPi.GPIO as io
import atexit
import requests

io.setmode(io.BCM)

pir_pin = 18
green_pin = 17
red_pin = 27

io.setup(pir_pin, io.IN)
io.setup(green_pin, io.OUT)
io.setup(red_pin, io.OUT)

def exit_handler():
    print "SHUTTING DOWN"
    io.output(green_pin, 0)
    io.output(red_pin, 0)

atexit.register(exit_handler)

while True:
    io.output(green_pin, 0)
    io.output(red_pin, 0)

    if io.input(pir_pin):
        print("PIR ALARM")
        requests.post("pipingpong.cfapps.io/activity", data={'active': 1})
        io.output(green_pin, 1)
    else:
        print("NADA")
        requests.post("pipingpong.cfapps.io/activity", data={'active': 0})
        io.output(red_pin, 1)

    time.sleep(0.5)
