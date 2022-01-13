from subscribe import subscribe
from publish import publish
from time import sleep
from signal import pause
from trafficlight import blink_red, blink_green, blink_amber

broker = "test.mosquitto.org"
topic = "trafficlight/bradford"

try:
    while True:
        # subscribe to the topic
        subscribe(broker, topic)

        # publish traffic data to the broker on the topic
        publish(broker, topic, "{light: amber, signal: OFF, duration: 0}")
        publish(broker, topic, "{light: red, signal: ON, duration: 5}")
        blink_red()  # Change traffic light to Red for 5 seconds
        sleep(5)
        publish(broker, topic, "{light: red, signal: OFF, duration: 0}")
        publish(broker, topic, "{light: amber, signal: ON, duration: 2}")
        blink_amber()  # Change traffic light to Amber for 2 seconds
        sleep(2)
        publish(broker, topic, "{light: amber, signal: OFF, duration: 0}")
        publish(broker, topic, "{light: green, signal: ON, duration: 10}")
        blink_green()  # Change Traffic light to Green for 10 seconds
        sleep(10)
        pause()
except KeyboardInterrupt:
    pass
