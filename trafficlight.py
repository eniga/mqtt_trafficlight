import RPi.GPIO as gpio
import time

def trafficLight(green, yellow, red):
    gpio.output(red, gpio.HIGH)