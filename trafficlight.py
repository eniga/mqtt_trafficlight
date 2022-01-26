from gpiozero import LED
from time import sleep

redlight = LED(13)
amberlight = LED(19)
greenlight = LED(26)


def blink_red(duration=5):
    redlight.on()  # default duration of 5
    sleep(duration)
    redlight.off()


def blink_amber(duration=2):
    amberlight.on()  # default duration of 2
    sleep(duration)
    amberlight.off()


def blink_green(duration=10):
    greenlight.on()  # default duration of 10
    sleep(duration)
    greenlight.off()
