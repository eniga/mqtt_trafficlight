from gpiozero import LED
from time import sleep

redlight = LED(13)
amberlight = LED(19)
greenlight = LED(26)


def blink_red(duration=5):
    redlight.blink(1, duration)  # default duration of 5
    sleep(1)


def blink_amber(duration=2):
    amberlight.blink(1, duration)  # default duration of 2
    sleep(1)


def blink_green(duration=10):
    greenlight.blink(1, duration)  # default duration of 10
    sleep(1)
